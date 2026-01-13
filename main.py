import sys
from PySide6.QtWidgets import QApplication
from core.settings_manager import SettingsManager
from core.data_manager import DataManager
from core.scheduler import Scheduler
from core.report_manager import ReportManager
from ui.tray import SystemTray
from ui.input_window import InputWindow
from ui.settings_window import SettingsWindow

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    # Core Components
    settings_manager = SettingsManager()
    data_manager = DataManager()
    scheduler = Scheduler(settings_manager)

    # UI Components
    input_window = InputWindow(data_manager, settings_manager)
    settings_window = SettingsWindow(settings_manager)
    tray = SystemTray(scheduler)
    report_manager = ReportManager()

    # Connect Signals
    
    # Scheduler triggers input
    scheduler.trigger_input.connect(input_window.show_window)
    
    # Tray actions
    tray.request_input.connect(input_window.show_window)
    tray.request_settings.connect(settings_window.show)
    tray.request_report.connect(report_manager.launch_report_interface)
    tray.request_exit.connect(app.quit)
    
    # Pause/Resume
    def handle_pause(should_pause):
        if should_pause:
            scheduler.pause()
        else:
            scheduler.resume()
    tray.toggle_pause.connect(handle_pause)

    # Settings updates
    # When settings dialog is accepted, we might need to update scheduler (e.g. interval changed)
    # The SettingsWindow updates the SettingsManager directly on save.
    # We just need to tell Scheduler to re-read settings or apply them.
    # We can connect the accepted signal of the dialog to scheduler.apply_settings
    settings_window.accepted.connect(scheduler.apply_settings)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
