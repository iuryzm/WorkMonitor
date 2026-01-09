from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QApplication, QCompleter
from PySide6.QtCore import Qt, Signal, QStringListModel
from PySide6.QtGui import QAction
from core.data_manager import DataManager
from core.settings_manager import SettingsManager

class InputWindow(QWidget):
    submitted = Signal(str)

    def __init__(self, data_manager: DataManager, settings_manager: SettingsManager):
        super().__init__()
        self.data_manager = data_manager
        self.settings_manager = settings_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Work Monitor")
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Style
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                color: #ffffff;
                border: 1px solid #555555;
                border-radius: 10px;
            }
            QLineEdit {
                background-color: #3b3b3b;
                border: 1px solid #555555;
                padding: 5px;
                border-radius: 5px;
                color: white;
            }
            QPushButton {
                background-color: #007acc;
                border: none;
                padding: 5px 15px;
                border-radius: 5px;
                color: white;
            }
            QPushButton:hover {
                background-color: #005f9e;
            }
        """)

        layout = QVBoxLayout()
        
        label = QLabel("What are you working on right now?")
        label.setStyleSheet("border: none; font-size: 14px; font-weight: bold;")
        layout.addWidget(label)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your activity...")
        self.input_field.returnPressed.connect(self.submit_activity)
        layout.addWidget(self.input_field)

        self.submit_btn = QPushButton("Log Activity")
        self.submit_btn.clicked.connect(self.submit_activity)
        layout.addWidget(self.submit_btn)

        self.setLayout(layout)
        
        # Completer
        self.completer = QCompleter()
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.input_field.setCompleter(self.completer)

    def show_window(self):
        # Update completer data
        activities = self.data_manager.get_unique_activities()
        model = QStringListModel(activities)
        self.completer.setModel(model)
        
        self.input_field.clear()
        
        # Center on screen or ensure visibility
        screen_geometry = QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)
        
        self.show()
        self.activateWindow()
        self.input_field.setFocus()
        
        if self.settings_manager.is_sound_enabled():
             QApplication.beep() 

    def submit_activity(self):
        text = self.input_field.text().strip()
        if text:
            self.data_manager.log_activity(text)
            self.submitted.emit(text)
        self.hide()
