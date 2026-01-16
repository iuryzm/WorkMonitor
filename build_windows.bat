@echo off
REM Ensure PyInstaller is installed
python -m pip install pyinstaller

REM Clean previous builds
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

REM Run PyInstaller using the spec file
pyinstaller WorkMonitor.spec

echo Build complete. Executable is in dist\WorkMonitor.exe
pause
