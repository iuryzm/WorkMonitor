import csv
import os
from datetime import datetime

LOG_DIR = os.path.expanduser("~/.workmonitor")
LOG_FILE = os.path.join(LOG_DIR, 'work_log.csv')

class DataManager:
    def __init__(self):
        self.ensure_log_directory()
        self.ensure_log_file()

    def ensure_log_directory(self):
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)

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

    def get_recent_activities(self, limit=50):
        activities = []
        if os.path.exists(LOG_FILE):
             with open(LOG_FILE, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader, None)
                all_rows = list(reader)
                
             seen = set()
             for row in reversed(all_rows):
                 if len(row) > 1:
                     activity = row[1]
                     if activity and activity not in seen:
                         activities.append(activity)
                         seen.add(activity)
                         if len(activities) >= limit:
                             break
        return activities
