# Chrome Features Parser

A tool to parse and display Chrome browser features, Blink features, Blink settings, and preferences.

## 安装依赖

```bash
pip3 install -r requirements.txt
```

## 运行

```bash
python3 run.py
```

This will download the latest Chrome source files, parse them, and generate an HTML file at `build/index.html`.

## Features

- **Chrome features**: Enable with `--enable-features`, disable with `--disable-features`
- **Blink features**: Enable with `--enable-blink-features`, disable with `--disable-blink-features`  
- **Blink settings**: Modify with `--blink-settings`
- **Preferences**: JSON preferences in the Chrome profile