# Chrome Features Parser

A tool to parse and display Chrome switches, features, Blink features, settings, and preferences from Chrome source code.

## Requirements

- Python 3.x
- Doxygen (required for XML parsing of Chrome switches and features)

Install Doxygen:
- **Windows**: Download from [doxygen.nl](https://www.doxygen.nl/download.html) or use `choco install doxygen`
- **macOS**: `brew install doxygen`
- **Linux**: `sudo apt-get install doxygen` or equivalent

## Quick Start

```bash
pip install -r requirements.txt
python run.py
```

Generates HTML file at `build/index.html`

## Supported Chrome Switch Types

- **Command Line Switches** - Various Chrome startup flags and options
- **Chrome Features** - Enable: `--enable-features=FeatureName` / Disable: `--disable-features=FeatureName`
- **Blink Features** - Enable: `--enable-blink-features=FeatureName` / Disable: `--disable-blink-features=FeatureName`  
- **Blink Settings** - Configure: `--blink-settings=setting=value`
- **Preferences** - JSON preferences in Chrome profile directory