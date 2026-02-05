# WorkMonitor

WorkMonitor is a cross-platform desktop application designed to help you track your daily activities. It periodically prompts you to log what you are doing, saving the data to a CSV file. It sits quietly in your system tray and offers customizable settings.

## Features

- **Periodic Prompts**: An always-on-top input window appears at set intervals to ask for your current activity.
- **Activity Logging**: All entries are saved with timestamps to `~/.workmonitor/work_log.csv` (Unix) or `%USERPROFILE%\.workmonitor\work_log.csv` (Windows).
- **Autocomplete**: Remembers previous entries to speed up logging.
- **Activity History**:
    - Navigate through recent entries using Up/Down arrow keys.
    - Quick access to past unique activities via a history button.
- **System Tray Integration**:
    - **Countdown**: Tooltip shows time remaining until the next prompt.
    - **New Entry**: Manually trigger the input window.
    - **Report**: Generate visual reports of your activity.
    - **Pause/Resume**: Temporarily stop the prompts (e.g., during meetings or breaks).
    - **Settings**: Configure the prompt interval and sound effects.
    - **Exit**: Close the application.
- **Cross-Platform**: Runs on Linux and Windows using PySide6.
- **Startup Support**: Windows build script includes option to create a Startup shortcut.

## Requirements

- Python 3.x
- PySide6

## Installation

1.  Clone the repository or download the source code.
2.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the application:

    ```bash
    python main.py
    ```

2.  The application will start minimized to the system tray. Use the tray icon (right-click) to access the menu.
3.  When the prompt appears, type your activity and press Enter to save.

## Build Executable

To create a standalone executable, **you must run the build script on the operating system you are building for**. PyInstaller does not support cross-compilation (e.g., you cannot build a Windows .exe from Linux easily).

### Linux

Run the build script regarding your terminal:

```bash
./build_linux.sh
```

The executable will be located in `dist/WorkMonitor`.

### Windows

Run the build script:

```bat
build_windows.bat
```

The executable will be located in `dist\WorkMonitor.exe`.

## Development

To run the tests:

```bash
python -m unittest discover tests
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
