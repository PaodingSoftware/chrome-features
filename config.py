#!/usr/bin/env python3
"""
Configuration file for Chrome Features Parser
"""

# Network settings
CHROME_REPO_BASE_URL = "https://raw.githubusercontent.com/chromium/chromium/main"
TIMEOUT_SECONDS = 30

# Directory structure
DIRECTORIES = ['src', 'xml', 'build']

# File mappings
CORE_FILES = [
    "content/public/common/content_features.cc",
    "third_party/blink/common/features.cc",
    "third_party/blink/renderer/platform/runtime_enabled_features.json5",
    "third_party/blink/renderer/core/frame/settings.json5",
    "chrome/common/pref_names.h",
]

# XML files for parsing
NAMESPACE_XML_FILES = [
    'xml/namespaceswitches.xml',
    'xml/namespaceheadless_1_1switches.xml',
    'xml/namespaceheadless.xml',
    'xml/namespaceinput_1_1switches.xml',
    'xml/namespacesyncer.xml',
    'xml/namespaceembedder__support.xml'
]

CHROME_FEATURES_XML_FILES = [
    'xml/namespacefeatures.xml',
    'xml/namespaceblink_1_1features.xml'
]

# Doxygen configuration
DOXYGEN_CONFIG = """
GENERATE_HTML=NO
GENERATE_LATEX=NO
GENERATE_XML=YES
QUIET=YES
INPUT=src
FILE_PATTERNS=*.cc,*.h
"""

# Source mapping patterns for switches
SOURCE_MAPPING_PATTERNS = {
    'chrome/common/chrome_switches': 'Chrome',
    'content/public/common/content_switches': 'Content',
    'gpu/config/gpu_switches': 'GPU',
    'ui/base/ui_base_switches': 'UI',
    'media/base/media_switches': 'Media',
    'components/viz/common/switches': 'Viz',
    'ui/gl/gl_switches': 'UI/GL',
    'cc/base/switches': 'CC',
    'base/base_switches': 'Base',
    'ash/constants/ash_switches': 'Ash',
    'chromeos/constants/chromeos_switches': 'ChromeOS',
    'extensions/common/switches': 'Extensions',
    'autofill': 'Autofill',
    'network_session_configurator': 'Network',
    'policy': 'Policy',
    'input/switches': 'Input',
    'sync': 'Sync',
    'headless': 'Headless',
    'embedder_support': 'Embedder Support',
    'component_updater': 'Component Updater',
    'enterprise': 'Enterprise',
    'android_webview': 'Android WebView',
    'apps/switches': 'Apps',
    'keyboard': 'Keyboard',
    'i18n': 'I18n',
    'test': 'Test',
    'android_sms': 'Android SMS',
    'borealis': 'Borealis',
    'device_trust': 'Device Trust',
    'extension_updater': 'Extension Updater',
    'google.*switches': 'Google',
    'ip_protection': 'IP Protection',
    'nearby_sharing|nearby_share': 'Nearby Share',
    'modules': 'Modules',
    'predictors': 'Predictors',
    'bound_session': 'Bound Session',
    'webauthn': 'WebAuthn',
    'chromecast': 'Chromecast',
    'assistant': 'Assistant',
    'device_sync': 'Device Sync',
    'mahi': 'Mahi',
    'dbus': 'DBus',
    'machine_learning|ml_switches': 'Machine Learning',
    'browser_sync': 'Browser Sync',
    'cast_streaming': 'Cast Streaming',
    'client_hints': 'Client Hints',
    'crash': 'Crash',
    'data_sharing': 'Data Sharing',
    'dom_distiller': 'DOM Distiller',
    'error_page': 'Error Page',
    'feedback': 'Feedback',
    'command_handler': 'Command Handler',
    'heap_profiling': 'Heap Profiling',
    'infobars': 'Infobars',
    'invalidation': 'Invalidation',
    'media_router': 'Media Router',
    'metrics': 'Metrics',
    'nacl': 'NaCl',
    'ntp_tiles': 'NTP Tiles',
    'optimization_guide': 'Optimization Guide',
    'os_crypt': 'OS Crypt',
    'page_content_annotations': 'Page Content Annotations',
    'password_manager': 'Password Manager',
    'permissions': 'Permissions',
    'regional_capabilities': 'Regional Capabilities',
    'safe_browsing|safebrowsing': 'Safe Browsing',
    'search_engines': 'Search Engines',
    'search_provider_logos': 'Search Provider Logos',
    'signin': 'Signin',
    'sync_bookmarks': 'Sync Bookmarks',
    'tracing': 'Tracing',
    'translate': 'Translate',
    'trusted_vault': 'Trusted Vault',
    'ui_devtools': 'UI DevTools',
    'variations': 'Variations',
    'demo': 'Demo',
    'flags_ui': 'Flags UI',
    'shell': 'Shell',
    'web_test': 'Web Test',
    'gamepad': 'Gamepad',
    'device/vr': 'VR',
    'fuchsia': 'Fuchsia',
    'gaia': 'Gaia',
    'gcm|gservices': 'GCM',
    'command_buffer': 'GPU Command Buffer',
    'ios': 'iOS',
    'capture': 'Media Capture',
    'mf_video_encoder': 'Media Foundation',
    'midi': 'MIDI',
    'mojo': 'Mojo',
    'ppapi': 'PPAPI',
    'remoting': 'Remoting',
    'sandbox': 'Sandbox',
    'hid': 'HID',
    'services/network': 'Network Service',
    'resource_coordinator': 'Resource Coordinator',
    'service_manager': 'Service Manager',
    'webnn': 'WebNN',
    'skia': 'Skia',
    'third_party/blink': 'Blink',
    'forcedark': 'Force Dark',
    'cros_system_api': 'ChromeOS System API',
    'modemfwd': 'Modem Forward',
    'accessibility': 'Accessibility',
    'compositor': 'Compositor',
    'display': 'Display',
    'events': 'Events',
    'ui/gfx': 'Graphics',
    'ozone': 'Ozone',
    'views': 'Views',
    'wm/core': 'Window Manager',
}

# File paths
SWITCHES_FILE = 'switches.txt'
TEMPLATE_FILE = 'template.html'
OUTPUT_FILE = 'build/index.html'
OBSIDIAN_SWITCHES_FILE = 'build/chrome_switches_review.md'
PREFS_XML_FILE = 'xml/namespaceprefs.xml'
CONTENT_FEATURES_XML = 'xml/content__public__common__content__features_8cc.xml'
BLINK_FEATURES_JSON = 'src/third_party_blink_renderer_platform_runtime_enabled_features.json5'
BLINK_SETTINGS_JSON = 'src/third_party_blink_renderer_core_frame_settings.json5'
