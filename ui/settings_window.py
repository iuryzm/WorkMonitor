from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QSpinBox, QCheckBox, QDialogButtonBox
from core.settings_manager import SettingsManager

class SettingsWindow(QDialog):
    def __init__(self, settings_manager: SettingsManager):
        super().__init__()
        self.settings_manager = settings_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Settings")
        layout = QVBoxLayout()

        # Interval
        layout.addWidget(QLabel("Interval (minutes):"))
        self.interval_spin = QSpinBox()
        self.interval_spin.setRange(1, 1440) # 1 min to 24 hours
        self.interval_spin.setValue(self.settings_manager.get_interval())
        layout.addWidget(self.interval_spin)

        # Sound
        self.sound_check = QCheckBox("Enable Sound Notification")
        self.sound_check.setChecked(self.settings_manager.is_sound_enabled())
        layout.addWidget(self.sound_check)

        # Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.save_settings)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def save_settings(self):
        self.settings_manager.set_interval(self.interval_spin.value())
        self.settings_manager.set_sound_enabled(self.sound_check.isChecked())
        self.accept()
