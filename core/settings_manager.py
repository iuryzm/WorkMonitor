import json
import os

SETTINGS_FILE = 'settings.json'

class SettingsManager:
    def __init__(self):
        self.settings = {
            "interval_minutes": 30,
            "sound_enabled": True
        }
        self.load_settings()

    def load_settings(self):
        if os.path.exists(SETTINGS_FILE):
            try:
                with open(SETTINGS_FILE, 'r') as f:
                    self.settings.update(json.load(f))
            except json.JSONDecodeError:
                pass  # Use defaults if file is corrupt

    def save_settings(self):
        with open(SETTINGS_FILE, 'w') as f:
            json.dump(self.settings, f, indent=4)

    def get_interval(self):
        return self.settings.get("interval_minutes", 30)

    def set_interval(self, minutes):
        self.settings["interval_minutes"] = minutes
        self.save_settings()

    def is_sound_enabled(self):
        return self.settings.get("sound_enabled", True)

    def set_sound_enabled(self, enabled):
        self.settings["sound_enabled"] = enabled
        self.save_settings()
