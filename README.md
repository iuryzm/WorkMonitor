# WorkMonitor

WorkMonitor is a cross-platform desktop application designed to help you track your daily activities. It periodically prompts you to log what you are doing, saving the data to a CSV file. It sits quietly in your system tray and offers customizable settings.

## Features

- **Periodic Prompts**: An always-on-top input window appears at set intervals to ask for your current activity.
- **Activity Logging**: All entries are saved with timestamps to `work_log.csv`.
- **Autocomplete**: Remembers previous entries to speed up logging.
- **System Tray Integration**:
    - **New Entry**: Manually trigger the input window.
    - **Pause/Resume**: Temporarily stop the prompts (e.g., during meetings or breaks).
    - **Settings**: Configure the prompt interval and sound effects.
    - **Exit**: Close the application.
- **Cross-Platform**: Runs on Linux and Windows using PySide6.

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

## Development

To run the tests:

```bash
python -m unittest discover tests
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
