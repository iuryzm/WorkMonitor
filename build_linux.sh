#!/bin/bash

# Ensure PyInstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo "PyInstaller not found. Installing..."
    pip install pyinstaller
fi

# Clean previous builds
rm -rf build dist

# Run PyInstaller
pyinstaller WorkMonitor.spec

echo "Build complete. Executable is in dist/WorkMonitor"
