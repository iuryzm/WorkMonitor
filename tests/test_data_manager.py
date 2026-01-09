import unittest
import os
import shutil
from core.data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        # Backup existing log if any
        if os.path.exists('work_log.csv'):
            shutil.move('work_log.csv', 'work_log.csv.bak')
            
    def tearDown(self):
        if os.path.exists('work_log.csv'):
            os.remove('work_log.csv')
        if os.path.exists('work_log.csv.bak'):
            shutil.move('work_log.csv.bak', 'work_log.csv')

    def test_log_and_retrieve(self):
        dm = DataManager()
        dm.log_activity("Coding Python")
        dm.log_activity("Testing App")
        
        activities = dm.get_unique_activities()
        self.assertIn("Coding Python", activities)
        self.assertIn("Testing App", activities)
        self.assertEqual(len(activities), 2)

if __name__ == '__main__':
    unittest.main()
