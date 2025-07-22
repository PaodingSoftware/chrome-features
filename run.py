#!/usr/bin/env python3
"""
Chrome Features Parser
A tool to parse and display Chrome browser features, Blink features, and settings.
"""

import sys
import re
import subprocess
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Union, Any
from dataclasses import dataclass
import requests
import pyjson5
import markdown
from jinja2 import Template
from lxml import etree
import html

# Import configuration
from config import (
    CHROME_REPO_BASE_URL, TIMEOUT_SECONDS, DIRECTORIES, CORE_FILES, 
    NAMESPACE_XML_FILES, CHROME_FEATURES_XML_FILES, DOXYGEN_CONFIG,
    SOURCE_MAPPING_PATTERNS, SWITCHES_FILE, TEMPLATE_FILE, OUTPUT_FILE,
    OBSIDIAN_SWITCHES_FILE, PREFS_XML_FILE, CONTENT_FEATURES_XML,
    BLINK_FEATURES_JSON, BLINK_SETTINGS_JSON
)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class Feature:
    """Represents a Chrome or Blink feature."""
    name: str
    enabled_default: bool = False
    description: str = ""
    
@dataclass
class Switch:
    """Represents a Chrome command-line switch."""
    name: str
    description: str = ""
    source: str = ""
    variable: str = ""
    sources: List[str] = None
    
    def __post_init__(self):
        if self.sources is None:
            self.sources = [self.source] if self.source else []

@dataclass
class Setting:
    """Represents a Blink setting."""
    name: str
    initial: Union[str, bool, int] = ""
    type: str = ""


def ensure_directories() -> None:
    """Create necessary directories."""
    for dir_name in DIRECTORIES:
        Path(dir_name).mkdir(exist_ok=True)
        logger.info(f"Ensured directory exists: {dir_name}")


def clean_directories() -> None:
    """Clean existing files (except src directory to preserve downloads)."""
    for dir_name in ['xml', 'build']:
        dir_path = Path(dir_name)
        if dir_path.exists():
            for file in dir_path.glob('*'):
                if file.is_file():
                    file.unlink()
            logger.info(f"Cleaned directory: {dir_name}")


def get_switches_files() -> List[str]:
    """Read switches files from switches.txt."""
    switches_files = []
    try:
        with open(SWITCHES_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and line.startswith('./'):
                    # Remove ./ prefix and add to files list
                    file_path = line[2:]
                    switches_files.append(file_path)
        logger.info(f"Loaded {len(switches_files)} switches files from {SWITCHES_FILE}")
    except FileNotFoundError:
        logger.warning(f"{SWITCHES_FILE} not found, using empty switches file list")
    return switches_files


def download_file(file_path: str) -> bool:
    """Download a single file from Chrome repository."""
    url = f"{CHROME_REPO_BASE_URL}/{file_path}"
    filename = file_path.replace('/', '_')
    local_path = Path('src') / filename
    
    # Skip download if file already exists
    if local_path.exists():
        logger.info(f"Skipped (already exists): {filename}")
        return True
    
    try:
        response = requests.get(url, timeout=TIMEOUT_SECONDS)
        response.raise_for_status()
        with open(local_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        logger.info(f"Downloaded: {filename}")
        return True
    except requests.RequestException as e:
        logger.error(f"Error downloading {filename}: {e}")
        return False


def download_chrome_files() -> None:
    """Download Chrome source files."""
    switches_files = get_switches_files()
    
    files = switches_files + CORE_FILES
    
    logger.info(f"Downloading {len(files)} Chrome source files...")
    successful_downloads = 0
    
    for file_path in files:
        if download_file(file_path):
            successful_downloads += 1
    
    logger.info(f"Downloaded {successful_downloads}/{len(files)} files successfully")


def generate_doxygen_xml() -> bool:
    """Generate doxygen XML output."""
    logger.info("Generating Doxygen XML...")
    
    try:
        proc = subprocess.Popen(['doxygen', '-'], stdin=subprocess.PIPE, 
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = proc.communicate(input=DOXYGEN_CONFIG)
        
        if proc.returncode != 0:
            logger.error(f"Doxygen error: {stderr}")
            return False
            
        logger.info("Doxygen XML generation completed successfully")
        return True
    except FileNotFoundError:
        logger.warning("doxygen not found. Chrome features parsing will be limited.")
        return False


def clean_comment_text(comment_xml: str) -> str:
    """Clean and format comment text from XML."""
    # Convert <sp/> tags to spaces and remove other XML tags
    comment_text = re.sub(r'<sp/>', ' ', comment_xml)
    comment_text = re.sub(r'<[^>]+>', '', comment_text)
    # Clean up HTML entities
    comment_text = html.unescape(comment_text)
    comment_text = re.sub(r'^//', '', comment_text.strip())
    return comment_text.strip()


def get_description_from_xml(line_num: int, lines_element: List) -> List[str]:
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
                comment_text = clean_comment_text(comment_xml)
                if comment_text:
                    description.append(comment_text)
            else:
                break
        else:
            break
            
        current_line -= 1
    
    return list(reversed(description))


def parse_feature_from_memberdef(memberdef, lines_element: Optional[List]) -> Optional[Feature]:
    """Parse a single feature from memberdef XML element."""
    definition = memberdef.xpath('./definition/text()')
    if not definition or (definition[0] != 'features::BASE_FEATURE' and 
                         definition[0] != 'blink::features::BASE_FEATURE'):
        return None
    
    # Extract feature name
    param_types = memberdef.xpath('./param/type/text()')
    if len(param_types) < 2:
        return None
        
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
    
    return Feature(name=name, enabled_default=enabled, description=desc_text)


def parse_chrome_features() -> List[Dict[str, Any]]:
    """Parse Chrome features from XML files."""
    logger.info("Parsing Chrome features...")
    features = []
    
    xml_files = CHROME_FEATURES_XML_FILES
    
    for xml_file in xml_files:
        if not Path(xml_file).exists():
            logger.warning(f"XML file not found: {xml_file}, skipping")
            continue
            
        try:
            tree = etree.parse(xml_file)
            
            # Get the lines from the main content file for descriptions
            lines_element = None
            if Path(CONTENT_FEATURES_XML).exists():
                content_tree = etree.parse(CONTENT_FEATURES_XML)
                lines_element = content_tree.xpath('//codeline')
            
            # Parse member definitions
            for memberdef in tree.xpath('//memberdef'):
                feature = parse_feature_from_memberdef(memberdef, lines_element)
                if feature:
                    features.append({
                        'name': feature.name,
                        'enabled_default': feature.enabled_default,
                        'description': feature.description
                    })
                        
        except etree.XMLSyntaxError as e:
            logger.error(f"Error parsing {xml_file}: {e}")
            continue
    
    # Sort features by name for consistent display
    features.sort(key=lambda x: x['name'].lower())
    logger.info(f"Found {len(features)} Chrome features")
    
    return features


def get_source_mapping() -> Dict[str, str]:
    """Create source mapping from XML filenames to display names."""
    source_mapping = {}
    xml_dir = Path('xml')
    
    # Scan for all XML files that match switches pattern
    for xml_file in xml_dir.glob('*switches*8*.xml'):
        xml_name = xml_file.stem
        src_name = xml_name.replace('_8cc', '.cc').replace('_8h', '.h')
        src_name = src_name.replace('__', '/')
        
        # Find matching pattern
        display_name = 'Other'
        for pattern, name in SOURCE_MAPPING_PATTERNS.items():
            if '|' in pattern:
                # Handle regex patterns
                if any(p in src_name for p in pattern.split('|')):
                    display_name = name
                    break
            else:
                if pattern in src_name:
                    display_name = name
                    break
        
        if display_name == 'Other':
            # Fallback: extract meaningful name from path
            parts = src_name.replace('/', ' ').replace('_', ' ').split()
            display_name = ' '.join(word.capitalize() for word in parts if word not in ['switches', 'cc', 'h', 'common', 'public', 'core', 'base'])
            if not display_name:
                display_name = 'Other'
        
        src_key = src_name.replace('/', '_').replace('.', '_')
        source_mapping[src_key] = display_name
    
    return source_mapping


def load_xml_files_for_switches() -> Dict[str, List]:
    """Load all XML files for switches parsing."""
    all_lines_elements = {}
    xml_dir = Path('xml')
    
    for xml_file in xml_dir.glob('*switches*8*.xml'):
        xml_name = xml_file.stem
        src_name = xml_name.replace('_8cc', '.cc').replace('_8h', '.h')
        src_name = src_name.replace('__', '/')
        
        try:
            content_tree = etree.parse(str(xml_file))
            lines = content_tree.xpath('//codeline')
            if lines:
                all_lines_elements[src_name] = lines
                logger.info(f"Loaded {len(lines)} code lines from {src_name}")
        except Exception as e:
            logger.error(f"Error loading {xml_file}: {e}")
    
    return all_lines_elements


def parse_switch_from_memberdef(memberdef, all_lines_elements: Dict[str, List], 
                               source_mapping: Dict[str, str]) -> Optional[Switch]:
    """Parse a single switch from memberdef XML element."""
    type_elem = memberdef.xpath('./type/text()')
    if not type_elem or (type_elem[0] != 'const char' and type_elem[0] != 'char'):
        return None
    
    name_elem = memberdef.xpath('./name/text()')
    initializer = memberdef.xpath('./initializer/text()')
    
    if not name_elem or not initializer:
        return None
    
    variable_name = name_elem[0]
    init_text = initializer[0]
    
    # Extract switch name from initializer (format: = "switch-name")
    if '"' not in init_text:
        return None
    
    matches = re.findall(r'"([^"]+)"', init_text)
    if not matches:
        return None
    
    switch_name = matches[0]
    
    # Get location info for description
    location_bodyfile = memberdef.xpath('./location/@bodyfile')
    location_bodystart = memberdef.xpath('./location/@bodystart')
    
    description = []
    desc_text = ''
    
    if location_bodyfile and location_bodystart:
        file_path = location_bodyfile[0]
        line_num = int(location_bodystart[0])
        
        # Find corresponding lines for descriptions
        for src_key, lines in all_lines_elements.items():
            if file_path.replace('src/', '').replace('/', '_').replace('.', '_') in src_key.replace('/', '_').replace('.', '_'):
                description = get_description_from_xml(line_num, lines)
                if description:
                    desc_text = markdown.markdown(html.escape('\n'.join(description)))
                break
    
    # Determine source based on file path using dynamic mapping
    source = 'Other'
    if location_bodyfile:
        file_path = location_bodyfile[0].lower()
        file_key = file_path.replace('src/', '').replace('/', '_').replace('.', '_')
        
        # Find matching source in our dynamic mapping
        for key, src_name in source_mapping.items():
            if key.replace('/', '_').replace('.', '_') in file_key:
                source = src_name
                break
    
    return Switch(name=switch_name, description=desc_text, source=source, 
                 variable=variable_name, sources=[source])


def parse_chrome_switches() -> List[Dict[str, Any]]:
    """Parse Chrome switches from XML files."""
    logger.info("Parsing Chrome switches...")
    switches = []
    switches_dict = {}  # To track unique switches and avoid duplicates
    
    # Dynamically discover all namespace XML files that contain switches
    xml_dir = Path('xml')
    namespace_xml_files = []
    
    # Find all namespace*switches*.xml files
    switches_namespaces = list(xml_dir.glob('namespace*switches*.xml'))
    
    # Also include some core namespace files that might contain switches
    core_namespaces = [
        'xml/namespaceswitches.xml',
        'xml/namespaceheadless.xml',
        'xml/namespacesyncer.xml',
        'xml/namespaceembedder__support.xml'
    ]
    
    # Combine and deduplicate
    all_files = [str(f) for f in switches_namespaces] + core_namespaces
    namespace_xml_files = list(set(f for f in all_files if Path(f).exists()))
    
    if not namespace_xml_files:
        logger.warning("No namespace XML files found, skipping Chrome switches parsing")
        return switches
    
    logger.info(f"Found {len(namespace_xml_files)} namespace XML files to parse")
    
    try:
        # Get source mapping and load XML files
        source_mapping = get_source_mapping()
        all_lines_elements = load_xml_files_for_switches()
        
        logger.info(f"Found {len(source_mapping)} source mappings")
        
        # Parse all member definitions from each namespace
        for namespace_xml in namespace_xml_files:
            if not Path(namespace_xml).exists():
                continue
                
            tree = etree.parse(namespace_xml)
            logger.info(f"Parsing switches from {namespace_xml}")
            
            # Parse all member definitions from the namespace
            for memberdef in tree.xpath('//memberdef'):
                switch = parse_switch_from_memberdef(memberdef, all_lines_elements, source_mapping)
                if switch:
                    # Only add if not already added (avoid duplicates)
                    if switch.name not in switches_dict:
                        switches_dict[switch.name] = {
                            'name': switch.name,
                            'description': switch.description,
                            'source': switch.source,
                            'variable': switch.variable,
                            'sources': switch.sources.copy()
                        }
                        switches.append(switches_dict[switch.name])
                    else:
                        # If switch already exists, add this source to the list
                        existing_switch = switches_dict[switch.name]
                        if switch.source not in existing_switch['sources']:
                            existing_switch['sources'].append(switch.source)
                            # Update description if current one is longer/better
                            if len(switch.description) > len(existing_switch['description']):
                                existing_switch['description'] = switch.description
                        
    except etree.XMLSyntaxError as e:
        logger.error(f"Error parsing switches XML: {e}")
    
    # Convert sources list to comma-separated string for display
    for switch in switches:
        if 'sources' in switch and len(switch['sources']) > 1:
            switch['source'] = ', '.join(sorted(switch['sources']))
    
    # Sort switches by name for consistent display
    switches.sort(key=lambda x: x['name'].lower())
    
    unique_switches = len(set(s['name'] for s in switches))
    logger.info(f"Found {len(switches)} switches total ({unique_switches} unique)")
    return switches


def parse_blink_features() -> List[Dict[str, Any]]:
    """Parse blink features from JSON5 files."""
    logger.info("Parsing Blink features...")
    
    try:
        # Load blink features
        with open(BLINK_FEATURES_JSON, 'r', encoding='utf-8') as f:
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
        logger.info(f"Found {len(processed_features)} Blink features")
        
        return processed_features
    
    except Exception as e:
        logger.error(f"Error parsing Blink features: {e}")
        return []


def parse_blink_settings() -> List[Dict[str, Any]]:
    """Parse blink settings from JSON5 file."""
    logger.info("Parsing Blink settings...")
    
    try:
        with open(BLINK_SETTINGS_JSON, 'r', encoding='utf-8') as f:
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
        logger.info(f"Found {len(processed_settings)} Blink settings")
        
        return processed_settings
    
    except Exception as e:
        logger.error(f"Error parsing Blink settings: {e}")
        return []


def parse_prefs() -> Dict[str, Any]:
    """Parse Chrome preferences from XML."""
    logger.info("Parsing preferences...")
    prefs = {}
    
    if not Path(PREFS_XML_FILE).exists():
        logger.warning(f"XML file not found: {PREFS_XML_FILE}, skipping preferences parsing")
        return prefs
    
    try:
        tree = etree.parse(PREFS_XML_FILE)
        
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
        
        logger.info(f"Found {len(prefs)} preference categories")
                            
    except etree.XMLSyntaxError as e:
        logger.error(f"Error parsing prefs XML: {e}")
    
    return prefs


def generate_html(chrome_switches: List[Dict[str, Any]], chrome_features: List[Dict[str, Any]], 
                 blink_features: List[Dict[str, Any]], blink_settings: List[Dict[str, Any]], 
                 prefs: Dict[str, Any]) -> None:
    """Generate HTML using Jinja2 template."""
    logger.info("Generating HTML...")
    
    try:
        with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
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
        
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(html_output)
        
        logger.info(f"HTML generated successfully at {OUTPUT_FILE}")
    
    except Exception as e:
        logger.error(f"Error generating HTML: {e}")
        raise


def generate_obsidian_switches_review(chrome_switches: List[Dict[str, Any]]) -> None:
    """Generate Obsidian Markdown file for switches review."""
    logger.info("Generating Obsidian switches review file...")
    
    try:
        # Create markdown content
        content = []
        content.append("# Chrome Switches Review")
        content.append("")
        content.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        content.append(f"Total switches: {len(chrome_switches)}")
        content.append("")
        content.append("## Instructions")
        content.append("- [ ] Check the checkbox after reviewing each switch")
        content.append("- [ ] Add notes in the 'Review Notes' column as needed")
        content.append("- [ ] Use tags like #important, #deprecated, #experimental for categorization")
        content.append("")
        
        # Group switches by source for better organization
        switches_by_source = {}
        for switch in chrome_switches:
            source = switch.get('source', 'Other')
            if source not in switches_by_source:
                switches_by_source[source] = []
            switches_by_source[source].append(switch)
        
        # Generate table for each source category
        checkbox_counter = 1  # Counter for unique checkbox IDs
        for source in sorted(switches_by_source.keys()):
            switches = switches_by_source[source]
            content.append(f"## {source} ({len(switches)} switches)")
            content.append("")
            
            # Table header
            content.append("| Reviewed | Switch Name | Variable | Description | Review Notes |")
            content.append("|----------|-------------|----------|-------------|--------------|")
            
            # Table rows
            for switch in sorted(switches, key=lambda x: x['name'].lower()):
                name = switch['name']
                variable = switch.get('variable', '')
                description = switch.get('description', '')
                
                # Clean description for table display (remove HTML and newlines)
                clean_desc = re.sub(r'<[^>]+>', '', description)
                clean_desc = clean_desc.replace('\n', ' ').replace('\r', '').strip()
                clean_desc = clean_desc.replace('|', '\\|')  # Escape pipe characters
                
                # Limit description length for readability
                if len(clean_desc) > 100:
                    clean_desc = clean_desc[:97] + "..."
                
                # Generate unique checkbox ID
                checkbox_id = f"switch_{checkbox_counter:04d}"
                checkbox_counter += 1
                
                content.append(f'| <input type="checkbox" unchecked id="{checkbox_id}"> | `{name}` | `{variable}` | {clean_desc} |  |')
            
            content.append("")
        
        # Add summary statistics
        content.append("## Review Progress")
        content.append("")
        content.append("### Statistics by Source")
        for source in sorted(switches_by_source.keys()):
            count = len(switches_by_source[source])
            content.append(f"- **{source}**: {count} switches")
        
        content.append("")
        content.append("### Review Checklist")
        content.append("- [ ] All switches reviewed")
        content.append("- [ ] Important switches identified and tagged")
        content.append("- [ ] Deprecated switches noted")
        content.append("- [ ] Documentation gaps identified")
        content.append("- [ ] Follow-up actions documented")
        
        # Write to file
        with open(OBSIDIAN_SWITCHES_FILE, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content))
        
        logger.info(f"Obsidian switches review file generated successfully at {OBSIDIAN_SWITCHES_FILE}")
    
    except Exception as e:
        logger.error(f"Error generating Obsidian switches review file: {e}")
        raise


def print_processing_summary(chrome_switches: List, chrome_features: List, 
                           blink_features: List, blink_settings: List, 
                           has_doxygen: bool) -> None:
    """Print processing summary."""
    logger.info("Processing Summary:")
    logger.info(f"- {len(chrome_switches)} Chrome switches")
    logger.info(f"- {len(chrome_features)} Chrome features")
    logger.info(f"- {len(blink_features)} Blink features")
    logger.info(f"- {len(blink_settings)} Blink settings")
    
    logger.info("Generated files:")
    logger.info(f"- HTML report: {OUTPUT_FILE}")
    if chrome_switches:
        logger.info(f"- Obsidian review file: {OBSIDIAN_SWITCHES_FILE}")
    
    if not has_doxygen:
        logger.warning("Note: Install doxygen to enable Chrome features and preferences parsing")
    logger.info("Processing completed successfully!")


def main() -> None:
    """Main function."""
    logger.info("Chrome Features Parser")
    logger.info("=" * 50)
    
    try:
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
        
        # Generate Obsidian switches review file if we have switches
        if chrome_switches:
            generate_obsidian_switches_review(chrome_switches)
        
        # Print summary
        print_processing_summary(chrome_switches, chrome_features, blink_features, blink_settings, has_doxygen)
        
    except Exception as e:
        logger.error(f"An error occurred during processing: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
