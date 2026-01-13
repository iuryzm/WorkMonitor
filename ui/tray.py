from PySide6.QtWidgets import QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Signal
import os

# Create a simple icon if none exists, or use system icon
class SystemTray(QSystemTrayIcon):
    request_input = Signal()
    request_settings = Signal()
    request_report = Signal()
    toggle_pause = Signal(bool) # True for pause, False for resume
    request_exit = Signal()

    def __init__(self, scheduler):
        super().__init__()
        self.scheduler = scheduler
        
        # Use a standard icon for now (or placeholder)
        # In a real app we'd load a .png
        # Using a standard system icon like 'document-save' or similar for linux compatibility testing
        if QIcon.hasThemeIcon("appointment-new"):
             self.setIcon(QIcon.fromTheme("appointment-new"))
        else:
             # Fallback or create pixmap on fly? 
             # For now let's try to set a text or just basic icon
             self.setIcon(QIcon.fromTheme("system-help")) # Placeholder

        self.setToolTip("Work Monitor")
        
        self.create_menu()
        self.show()

    def create_menu(self):
        self.menu = QMenu()
        
        new_entry_action = QAction("New Entry", self)
        new_entry_action.triggered.connect(self.request_input.emit)
        self.menu.addAction(new_entry_action)
        
        self.pause_action = QAction("Pause", self)
        self.pause_action.triggered.connect(self.handle_pause_toggle)
        self.menu.addAction(self.pause_action)
        
        settings_action = QAction("Settings", self)
        settings_action.triggered.connect(self.request_settings.emit)
        self.menu.addAction(settings_action)

        report_action = QAction("Relatório", self)
        report_action.triggered.connect(self.request_report.emit)
        self.menu.addAction(report_action)
        
        self.menu.addSeparator()
        
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.request_exit.emit)
        self.menu.addAction(exit_action)
        
        self.setContextMenu(self.menu)

    def handle_pause_toggle(self):
        if self.scheduler.is_paused():
            self.toggle_pause.emit(False) # Resume
            self.pause_action.setText("Pause")
        else:
            self.toggle_pause.emit(True) # Pause
            self.pause_action.setText("Resume")
