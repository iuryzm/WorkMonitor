import csv
import os
from datetime import datetime

LOG_FILE = 'work_log.csv'

class DataManager:
    def __init__(self):
        self.ensure_log_file()

    def ensure_log_file(self):
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Activity"])

    def log_activity(self, activity):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, activity])

    def get_unique_activities(self):
        activities = set()
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader, None)  # Skip header
                for row in reader:
                    if len(row) > 1:
                        activities.add(row[1])
        return sorted(list(activities))
