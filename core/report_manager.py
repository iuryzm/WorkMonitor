import csv
import sys
import json
import os
import webbrowser
from datetime import datetime
import tempfile


class ReportManager:
    def __init__(self, settings_manager=None):
        self.settings_manager = settings_manager
        self.log_file = 'work_log.csv'
        self.template_path = self.get_resource_path(os.path.join('core', 'templates', 'report_template.html'))

    def get_resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Root dir in dev
            
        return os.path.join(base_path, relative_path)

    def get_log_data(self):
        data = []
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader, None)  # Skip header
                    for row in reader:
                        if len(row) >= 2:
                            data.append({
                                'timestamp': row[0],
                                'activity': row[1]
                            })
            except Exception as e:
                print(f"Error reading log file: {e}")
        return data

    def launch_report_interface(self):
        data = self.get_log_data()
        json_data = json.dumps(data)

        if not os.path.exists(self.template_path):
            print(f"Template not found at {self.template_path}")
            return

        with open(self.template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()

        # Inject JSON data into the template
        # We look for {{ DATA_JSON | safe }} or just replace a marker
        # In the template I put {{ DATA_JSON | safe }} but since I'm not using Jinja2 engine, I'll do string replace.
        
        # Simple string replacement
        final_html = template_content.replace('[/* DATA_PLACEHOLDER */]', json_data)

        # Write to a temporary file or a fixed location?
        # A fixed location is better so it doesn't flood temp folder, and re-using it is fine.
        output_path = os.path.abspath("report_dashboard.html")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_html)

        webbrowser.open('file://' + output_path)
