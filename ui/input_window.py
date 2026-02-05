from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QApplication, QCompleter, QHBoxLayout, QMenu
from PySide6.QtCore import Qt, Signal, QStringListModel
from PySide6.QtGui import QAction, QKeyEvent
from core.data_manager import DataManager
from core.settings_manager import SettingsManager

class InputWindow(QWidget):
    submitted = Signal(str)

    def __init__(self, data_manager: DataManager, settings_manager: SettingsManager):
        super().__init__()
        self.data_manager = data_manager
        self.settings_manager = settings_manager
        self.history = []
        self.history_index = -1
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Log Activity")
        # Removed FramelessWindowHint and TranslucentBackground to use native window
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Tool)
        self.resize(400, 150) # Set a default reasonable size
        
        # Style
        # Adjusted style to work better with standard frame
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                color: #000000;
                font-family: 'Segoe UI', sans-serif;
            }
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: #333333;
            }
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                padding: 8px;
                border-radius: 4px;
                color: #333333;
            }
            QPushButton {
                background-color: #0078d4;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0063b1;
            }
            QToolTip {
                background-color: #ffffff;
                color: #333333;
                border: 1px solid #cccccc; 
            }
        """)

        layout = QVBoxLayout()
        
        label = QLabel("What are you working on right now?")
        # label.setStyleSheet("border: none; font-size: 14px; font-weight: bold;") # Style moved to global stylesheet
        layout.addWidget(label)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your activity...")
        self.input_field.returnPressed.connect(self.submit_activity)
        self.input_field.installEventFilter(self) # Install event filter for key navigation
        layout.addWidget(self.input_field)

        btn_layout = QHBoxLayout()
        
        self.submit_btn = QPushButton("Log Activity")
        self.submit_btn.clicked.connect(self.submit_activity)
        btn_layout.addWidget(self.submit_btn)

        self.history_btn = QPushButton("History")
        # self.history_btn.setFixedWidth(30) # Let it size to content
        self.history_btn.setToolTip("Show past activities")
        self.history_btn.clicked.connect(self.show_history_menu)
        btn_layout.addWidget(self.history_btn)
        
        layout.addLayout(btn_layout)

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
        
        # Load history
        self.history = self.data_manager.get_recent_activities(20)
        self.history_index = -1
        
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

    def show_history_menu(self):
        menu = QMenu(self)
        menu.setStyleSheet("""
            QMenu {
                background-color: #ffffff;
                color: #333333;
                border: 1px solid #cccccc;
            }
            QMenu::item {
                padding: 6px 24px;
            }
            QMenu::item:selected {
                background-color: #e6e6e6;
            }
        """)
        
        if not self.history:
            action = QAction("No history", self)
            action.setEnabled(False)
            menu.addAction(action)
        else:
            for activity in self.history:
                action = QAction(activity, self)
                action.triggered.connect(lambda checked=False, txt=activity: self.set_activity(txt))
                menu.addAction(action)
        
        menu.exec_(self.history_btn.mapToGlobal(self.history_btn.rect().bottomLeft()))

    def set_activity(self, text):
        self.input_field.setText(text)
        self.input_field.setFocus()
        
    def eventFilter(self, obj, event):
        if obj == self.input_field and event.type() == 6: # QEvent.KeyPress
            key = event.key()
            if key == Qt.Key_Up:
                self.navigate_history(1)
                return True
            elif key == Qt.Key_Down:
                self.navigate_history(-1)
                return True
        return super().eventFilter(obj, event)

    def navigate_history(self, direction):
        if not self.history:
            return
            
        new_index = self.history_index + direction
        
        # history[0] is most recent.
        # Key_Up (direction 1) should go to older (0 -> 1 -> 2)
        # Key_Down (direction -1) should go to newer (2 -> 1 -> 0 -> -1)
        
        if 0 <= new_index < len(self.history):
            self.history_index = new_index
            self.input_field.setText(self.history[self.history_index])
        elif new_index == -1:
            self.history_index = -1
            self.input_field.clear()
        # If out of bounds, do nothing or clamp. Here we clamp/limit.
        elif new_index >= len(self.history):
             # Stay at oldest
             pass
