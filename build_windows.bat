@echo off
REM Ensure dependencies are installed
python -m pip install -r requirements.txt

REM Clean previous builds
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

REM Run PyInstaller using the spec file
python -m PyInstaller WorkMonitor.spec

echo Build complete. Executable is in dist\WorkMonitor.exe

set /p msg="Create shortcut in Startup folder? (y/n): "
if /i "%msg%"=="y" (
    powershell -Command "$s=(New-Object -COM WScript.Shell).CreateShortcut('%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\WorkMonitor.lnk'); $s.TargetPath='%CD%\dist\WorkMonitor.exe'; $s.WorkingDirectory='%CD%'; $s.Save()"
    echo Shortcut created.
)
pause
