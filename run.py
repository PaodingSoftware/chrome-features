#!/usr/bin/env python3
"""
Chrome Features Parser
A tool to parse and display Chrome browser features, Blink features, and settings.
"""

import sys
import re
import subprocess
from datetime import datetime
from pathlib import Path
import requests
import pyjson5
import markdown
from jinja2 import Template
from lxml import etree
import html


def ensure_directories():
    """Create necessary directories."""
    for dir_name in ['src', 'xml', 'build']:
        Path(dir_name).mkdir(exist_ok=True)


def clean_directories():
    """Clean existing files."""
    for dir_name in ['src', 'xml', 'build']:
        dir_path = Path(dir_name)
        if dir_path.exists():
            for file in dir_path.glob('*'):
                if file.is_file():
                    file.unlink()


def download_chrome_files():
    """Download Chrome source files."""
    files = [
        # Chrome switches files
        "chrome/common/chrome_switches.cc",
        "chrome/common/chrome_switches.h",
        "content/public/common/content_switches.cc",
        "content/public/common/content_switches.h",
        "gpu/config/gpu_switches.cc",
        "gpu/config/gpu_switches.h",
        "ui/base/ui_base_switches.cc",
        "ui/base/ui_base_switches.h",
        "media/base/media_switches.cc",
        "media/base/media_switches.h",
        "components/viz/common/switches.cc",
        "components/viz/common/switches.h",
        "ui/gl/gl_switches.cc",
        "ui/gl/gl_switches.h",
        "cc/base/switches.cc",
        "cc/base/switches.h",
        "ash/constants/ash_switches.cc",
        "ash/constants/ash_switches.h",
        "chromeos/constants/chromeos_switches.cc",
        "chromeos/constants/chromeos_switches.h",
        "extensions/common/switches.cc",
        "extensions/common/switches.h",
        "components/autofill/core/common/autofill_switches.cc",
        "components/autofill/core/common/autofill_switches.h",
        "components/network_session_configurator/common/network_switches.cc",
        "components/network_session_configurator/common/network_switches.h",
        "components/policy/core/common/policy_switches.cc",
        "components/policy/core/common/policy_switches.h",
        
        # Chrome features files
        "content/public/common/content_features.cc",
        "third_party/blink/common/features.cc",
        
        # Blink features and settings files
        "third_party/blink/renderer/platform/runtime_enabled_features.json5",
        "third_party/blink/renderer/core/frame/settings.json5",
        
        # Preferences files
        "chrome/common/pref_names.h",
    ]
    
    print("Downloading Chrome source files...")
    for file_path in files:
        url = f"https://raw.githubusercontent.com/chromium/chromium/main/{file_path}"
        filename = file_path.replace('/', '_')
        local_path = Path('src') / filename
        
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            with open(local_path, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"Downloaded: {filename}")
        except requests.RequestException as e:
            print(f"Error downloading {filename}: {e}")
            sys.exit(1)


def generate_doxygen_xml():
    """Generate doxygen XML output."""
    print("Generating Doxygen XML...")
    doxygen_config = """
GENERATE_HTML=NO
GENERATE_LATEX=NO
GENERATE_XML=YES
QUIET=YES
INPUT=src
FILE_PATTERNS=*.cc,*.h
"""
    
    try:
        proc = subprocess.Popen(['doxygen', '-'], stdin=subprocess.PIPE, 
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = proc.communicate(input=doxygen_config)
        
        if proc.returncode != 0:
            print(f"Doxygen error: {stderr}")
            return False
            
        return True
    except FileNotFoundError:
        print("Warning: doxygen not found. Chrome features parsing will be limited.")
        return False


def get_description_from_xml(line_num, lines_element):
    """Extract description from XML comments."""
    description = []
    current_line = line_num - 1
    
    while current_line > 0:
        # Find the XML element for this line
        line_elem = None
        for line_el in lines_element:
            if int(line_el.get('lineno', 0)) == current_line:
                line_elem = line_el
                break
        
        if line_elem is not None:
            # Look for comment highlights
            highlights = line_elem.xpath('.//highlight[@class="comment"]')
            if highlights:
                # Extract text while preserving spaces by processing XML content
                # Use method='xml' to get the full XML including <sp/> tags
                comment_xml = etree.tostring(highlights[0], method='xml', encoding='unicode')
                # Convert <sp/> tags to spaces and remove other XML tags
                comment_text = re.sub(r'<sp/>', ' ', comment_xml)
                comment_text = re.sub(r'<[^>]+>', '', comment_text)
                # Clean up HTML entities
                comment_text = html.unescape(comment_text)
                comment_text = re.sub(r'^//', '', comment_text.strip())
                if comment_text:
                    description.append(comment_text.strip())
            else:
                break
        else:
            break
            
        current_line -= 1
    
    return list(reversed(description))


def parse_chrome_features():
    """Parse Chrome features from XML files."""
    print("Parsing Chrome features...")
    features = []
    
    xml_files = [
        'xml/namespacefeatures.xml',
        'xml/namespaceblink_1_1features.xml'
    ]
    
    for xml_file in xml_files:
        if not Path(xml_file).exists():
            print(f"XML file not found: {xml_file}, skipping Chrome features parsing")
            continue
            
        try:
            tree = etree.parse(xml_file)
            
            # Get the lines from the main content file for descriptions
            content_xml = 'xml/content__public__common__content__features_8cc.xml'
            lines_element = None
            if Path(content_xml).exists():
                content_tree = etree.parse(content_xml)
                lines_element = content_tree.xpath('//codeline')
            
            # Parse member definitions
            for memberdef in tree.xpath('//memberdef'):
                definition = memberdef.xpath('./definition/text()')
                if definition and (definition[0] == 'features::BASE_FEATURE' or 
                                definition[0] == 'blink::features::BASE_FEATURE'):
                    
                    # Extract feature name
                    param_types = memberdef.xpath('./param/type/text()')
                    if len(param_types) >= 2:
                        name = param_types[1].strip('"')
                        enabled = len(param_types) > 2 and param_types[2] == 'base::FEATURE_ENABLED_BY_DEFAULT'
                        
                        # Get line number and description
                        location = memberdef.xpath('./location/@line')
                        line_num = int(location[0]) if location else 0
                        
                        description = []
                        if lines_element:
                            description = get_description_from_xml(line_num, lines_element)
                        
                        desc_text = ''
                        if description:
                            desc_text = markdown.markdown(html.escape('\n'.join(description)))
                        
                        features.append({
                            'name': name,
                            'enabled_default': enabled,
                            'description': desc_text
                        })
                        
        except etree.XMLSyntaxError as e:
            print(f"Error parsing {xml_file}: {e}")
            continue
    
    # Sort features by name for consistent display
    features.sort(key=lambda x: x['name'].lower())
    
    return features


def parse_chrome_switches():
    """Parse Chrome switches from XML files."""
    print("Parsing Chrome switches...")
    switches = []
    
    # Parse from namespace switches XML (similar to parse_prefs approach)
    namespace_xml = 'xml/namespaceswitches.xml'
    if not Path(namespace_xml).exists():
        print("XML file not found: namespaceswitches.xml, skipping Chrome switches parsing")
        return switches
    
    try:
        tree = etree.parse(namespace_xml)
        
        # Get all switch source files for descriptions
        switch_xml_files = {
            'chrome_common_chrome_switches.cc': 'xml/chrome__common__chrome__switches_8cc.xml',
            'chrome_common_chrome_switches.h': 'xml/chrome__common__chrome__switches_8h.xml',
            'content_public_common_content_switches.cc': 'xml/content__public__common__content__switches_8cc.xml',
            'content_public_common_content_switches.h': 'xml/content__public__common__content__switches_8h.xml',
            'gpu_config_gpu_switches.cc': 'xml/gpu__config__gpu__switches_8cc.xml',
            'gpu_config_gpu_switches.h': 'xml/gpu__config__gpu__switches_8h.xml',
            'ui_base_ui_base_switches.cc': 'xml/ui__base__ui__base__switches_8cc.xml',
            'ui_base_ui_base_switches.h': 'xml/ui__base__ui__base__switches_8h.xml',
            'media_base_media_switches.cc': 'xml/media__base__media__switches_8cc.xml',
            'media_base_media_switches.h': 'xml/media__base__media__switches_8h.xml',
            'components_viz_common_switches.cc': 'xml/components__viz__common__switches_8cc.xml',
            'components_viz_common_switches.h': 'xml/components__viz__common__switches_8h.xml',
            'ui_gl_gl_switches.cc': 'xml/ui__gl__gl__switches_8cc.xml',
            'ui_gl_gl_switches.h': 'xml/ui__gl__gl__switches_8h.xml',
            'cc_base_switches.cc': 'xml/cc__base__switches_8cc.xml',
            'cc_base_switches.h': 'xml/cc__base__switches_8h.xml',
            'ash_constants_ash_switches.cc': 'xml/ash__constants__ash__switches_8cc.xml',
            'ash_constants_ash_switches.h': 'xml/ash__constants__ash__switches_8h.xml',
            'chromeos_constants_chromeos_switches.cc': 'xml/chromeos__constants__chromeos__switches_8cc.xml',
            'chromeos_constants_chromeos_switches.h': 'xml/chromeos__constants__chromeos__switches_8h.xml',
            'extensions_common_switches.cc': 'xml/extensions__common__switches_8cc.xml',
            'extensions_common_switches.h': 'xml/extensions__common__switches_8h.xml',
            'components_autofill_core_common_autofill_switches.cc': 'xml/components__autofill__core__common__autofill__switches_8cc.xml',
            'components_autofill_core_common_autofill_switches.h': 'xml/components__autofill__core__common__autofill__switches_8h.xml',
            'components_network_session_configurator_common_network_switches.cc': 'xml/components__network__session__configurator__common__network__switches_8cc.xml',
            'components_network_session_configurator_common_network_switches.h': 'xml/components__network__session__configurator__common__network__switches_8h.xml',
            'components_policy_core_common_policy_switches.cc': 'xml/components__policy__core__common__policy__switches_8cc.xml',
            'components_policy_core_common_policy_switches.h': 'xml/components__policy__core__common__policy__switches_8h.xml'
        }
        
        all_lines_elements = {}
        for src_name, xml_path in switch_xml_files.items():
            if Path(xml_path).exists():
                try:
                    content_tree = etree.parse(xml_path)
                    lines = content_tree.xpath('//codeline')
                    if lines:  # Only add if we found codelines
                        all_lines_elements[src_name] = lines
                        print(f"Loaded {len(lines)} code lines from {src_name}")
                except Exception as e:
                    print(f"Error loading {xml_path}: {e}")
        
        # Parse all member definitions from the namespace
        for memberdef in tree.xpath('//memberdef'):
            type_elem = memberdef.xpath('./type/text()')
            if type_elem and type_elem[0] == 'const char':
                name_elem = memberdef.xpath('./name/text()')
                initializer = memberdef.xpath('./initializer/text()')
                
                if name_elem and initializer:
                    variable_name = name_elem[0]
                    init_text = initializer[0]
                    
                    # Extract switch name from initializer (format: = "switch-name")
                    if '"' in init_text:
                        matches = re.findall(r'"([^"]+)"', init_text)
                        if matches:
                            switch_name = matches[0]
                            
                            # Get location info for description
                            location_bodyfile = memberdef.xpath('./location/@bodyfile')
                            location_bodystart = memberdef.xpath('./location/@bodystart')
                            
                            description = []
                            desc_text = ''
                            
                            if location_bodyfile and location_bodystart:
                                file_path = location_bodyfile[0]
                                line_num = int(location_bodystart[0])
                                
                                # Convert file path to source name key
                                file_key = file_path.replace('src/', '').replace('/', '_').replace('.', '_')
                                
                                # Find corresponding lines for descriptions
                                for src_key, lines in all_lines_elements.items():
                                    if src_key.replace('.', '_') == file_key:
                                        description = get_description_from_xml(line_num, lines)
                                        if description:
                                            desc_text = markdown.markdown(html.escape('\n'.join(description)))
                                        break
                            
                            # Determine source based on file path
                            source = 'Other'
                            if location_bodyfile:
                                file_path_lower = location_bodyfile[0].lower()
                                if 'chrome' in file_path_lower and 'chrome_switches' in file_path_lower:
                                    source = 'Chrome'
                                elif 'content' in file_path_lower:
                                    source = 'Content'
                                elif 'gpu' in file_path_lower:
                                    source = 'GPU'
                                elif 'ui' in file_path_lower and 'ui_base' in file_path_lower:
                                    source = 'UI'
                                elif 'media' in file_path_lower:
                                    source = 'Media'
                                elif 'viz' in file_path_lower:
                                    source = 'Viz'
                                elif 'ui' in file_path_lower and 'gl' in file_path_lower:
                                    source = 'UI/GL'
                                elif 'cc_base' in file_path_lower:
                                    source = 'CC'
                                elif 'ash' in file_path_lower:
                                    source = 'Ash'
                                elif 'chromeos' in file_path_lower:
                                    source = 'ChromeOS'
                                elif 'extensions' in file_path_lower:
                                    source = 'Extensions'
                                elif 'autofill' in file_path_lower:
                                    source = 'Autofill'
                                elif 'network' in file_path_lower:
                                    source = 'Network'
                                elif 'policy' in file_path_lower:
                                    source = 'Policy'
                            
                            switches.append({
                                'name': switch_name,
                                'description': desc_text,
                                'source': source,
                                'variable': variable_name
                            })
                        
    except etree.XMLSyntaxError as e:
        print(f"Error parsing switches XML: {e}")
    
    # Sort switches by name for consistent display
    switches.sort(key=lambda x: x['name'].lower())
    
    print(f"Found {len(switches)} switches total")
    return switches


def parse_blink_features():
    """Parse blink features from JSON5 files."""
    print("Parsing Blink features...")
    
    # Load blink features
    with open('src/third_party_blink_renderer_platform_runtime_enabled_features.json5', 'r', encoding='utf-8') as f:
        content = f.read()
        blink_features = pyjson5.loads(content)
    
    # Parse descriptions from comments
    desc = []
    features_data = blink_features.get('data', [])
    
    lines = content.split('\n')
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('//'):
            desc.append(stripped[2:].strip())
        elif desc and 'name:' in line and '"' in line:
            # Extract feature name
            name_match = re.search(r'name:\s*"([^"]+)"', line)
            if name_match:
                feature_name = name_match.group(1)
                # Find the feature in data and add description
                for feature in features_data:
                    if isinstance(feature, dict) and feature.get('name') == feature_name:
                        if desc:
                            feature['description'] = markdown.markdown(html.escape('\n'.join(desc)))
                        break
            desc = []
        elif stripped != '{':
            desc = []
    
    # Process features for template
    processed_features = []
    for feature in features_data:
        if isinstance(feature, dict) and 'name' in feature:
            processed_features.append({
                'name': feature['name'],
                'description': feature.get('description', ''),
                'enabled_default': feature.get('status') == 'stable'
            })
    
    # Sort features by name for consistent display
    processed_features.sort(key=lambda x: x['name'].lower())
    
    return processed_features


def parse_blink_settings():
    """Parse blink settings from JSON5 file."""
    print("Parsing Blink settings...")
    
    with open('src/third_party_blink_renderer_core_frame_settings.json5', 'r', encoding='utf-8') as f:
        blink_settings = pyjson5.loads(f.read())
    
    processed_settings = []
    for setting in blink_settings.get('data', []):
        if isinstance(setting, dict) and 'name' in setting:
            initial_val = setting.get('initial')
            if isinstance(initial_val, str) and initial_val.startswith("'") and initial_val.endswith("'"):
                initial_val = initial_val[1:-1]
                
            processed_settings.append({
                'name': setting['name'],
                'initial': initial_val,
                'type': setting.get('type', '')
            })
    
    # Sort settings by name for consistent display
    processed_settings.sort(key=lambda x: x['name'].lower())
    
    return processed_settings


def parse_prefs():
    """Parse Chrome preferences from XML."""
    print("Parsing preferences...")
    prefs = {}
    
    xml_file = 'xml/namespaceprefs.xml'
    if not Path(xml_file).exists():
        print("XML file not found: namespaceprefs.xml, skipping preferences parsing")
        return prefs
    
    try:
        tree = etree.parse(xml_file)
        
        for memberdef in tree.xpath('//memberdef'):
            type_elem = memberdef.xpath('./type/text()')
            if type_elem and (type_elem[0] == 'char' or type_elem[0] == 'constexpr char'):
                initializer = memberdef.xpath('./initializer/text()')
                if initializer and '"' in initializer[0]:
                    # Extract preference name from quotes
                    matches = re.findall(r'"([^"]+)"', initializer[0])
                    if matches:
                        pref_name = matches[0]
                        keys = pref_name.split('.')
                        
                        # Build nested structure
                        current_dict = prefs
                        for key in keys[:-1]:
                            if key not in current_dict:
                                current_dict[key] = {}
                            elif not isinstance(current_dict[key], dict):
                                current_dict[key] = {}
                            current_dict = current_dict[key]
                        
                        # Set final key
                        if keys:
                            current_dict[keys[-1]] = ""
                            
    except etree.XMLSyntaxError as e:
        print(f"Error parsing prefs XML: {e}")
    
    return prefs


def generate_html(chrome_switches, chrome_features, blink_features, blink_settings, prefs):
    """Generate HTML using Jinja2 template."""
    print("Generating HTML...")
    
    with open('template.html', 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    template = Template(template_content)
    
    html_output = template.render(
        chrome_switches=chrome_switches,
        chrome_features=chrome_features,
        blink_features=blink_features,
        blink_settings=blink_settings,
        prefs=prefs,
        current_date=datetime.now().strftime('%Y-%m-%d')
    )
    
    with open('build/index.html', 'w', encoding='utf-8') as f:
        f.write(html_output)
    
    print("HTML generated successfully at build/index.html")


def main():
    """Main function."""
    print("Chrome Features Parser")
    print("=====================")
    
    # Setup
    ensure_directories()
    clean_directories()
    
    # Download and process
    download_chrome_files()
    has_doxygen = generate_doxygen_xml()
    
    # Parse data
    chrome_switches = parse_chrome_switches() if has_doxygen else []
    chrome_features = parse_chrome_features() if has_doxygen else []
    blink_features = parse_blink_features()
    blink_settings = parse_blink_settings()
    prefs = parse_prefs() if has_doxygen else {}
    
    # Generate output
    generate_html(chrome_switches, chrome_features, blink_features, blink_settings, prefs)
    
    print("Processing Summary:")
    print(f"- {len(chrome_switches)} Chrome switches")
    print(f"- {len(chrome_features)} Chrome features")
    print(f"- {len(blink_features)} Blink features")
    print(f"- {len(blink_settings)} Blink settings")
    if not has_doxygen:
        print("Note: Install doxygen to enable Chrome features and preferences parsing")
    print("Done!")


if __name__ == '__main__':
    main()
