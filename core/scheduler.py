from PySide6.QtCore import QObject, QTimer, Signal
from core.settings_manager import SettingsManager

class Scheduler(QObject):
    trigger_input = Signal()

    def __init__(self, settings_manager: SettingsManager):
        super().__init__()
        self.settings_manager = settings_manager
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.trigger_input.emit)
        self.paused = False
        self.apply_settings()

    def apply_settings(self):
        # Convert minutes to milliseconds
        interval_ms = self.settings_manager.get_interval() * 60 * 1000
        if interval_ms > 0 and not self.paused:
             self.timer.start(interval_ms)
        else:
            self.timer.stop()

    def pause(self):
        self.paused = True
        self.timer.stop()

    def resume(self):
        self.paused = False
        self.apply_settings()

    def is_paused(self):
        return self.paused

    def get_remaining_time(self):
        if self.paused or not self.timer.isActive():
            return -1
        return self.timer.remainingTime()
