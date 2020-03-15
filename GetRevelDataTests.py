import unittest
import warnings

import mock as mock
import pandas as pd

from GetRevelData import GetRevelData
from fake_affidavit import fake_affidavit

warnings.simplefilter(action='ignore', category=FutureWarning)

fake_devices = pd.DataFrame(
    {'id': [1, 2, 3], 'name': ['truck1', 'truck2', 'truck3'], 'group_name': ['group1', 'group1', 'group1']})


class MyTestCase(unittest.TestCase):
    @mock.patch('GetRevelData.get_devices', return_value=fake_devices)
    @mock.patch('GetRevelData.GetRevelData.get_revel_data', return_value=fake_affidavit)
    def setUp(self, fake_get_devices, fake_get_revel_data):
        self.start = '2/1/2020'
        self.end = '2/7/2020'
        self.filename = 'data/cet/2020Week8.xlsx'
        self.report = GetRevelData(self.start, self.end, self.filename)

    def test_correct_input_data(self):
        self.assertEqual(self.start, self.report.start, 'Incorrect start date')
        self.assertEqual(self.end, self.report.end, 'Incorrect end date')
        self.assertEqual(self.filename, self.report.filename, 'Incorrect filename')

    def test_correct_cet_df(self):
        num_entries_in_cet_report = len(self.report.cet_df.index)
        self.assertEqual(1, num_entries_in_cet_report, "Incorrect number of routes")

    def test_devices(self):
        num_devices = len(self.report.devices_df.index)
        self.assertEqual(3, num_devices, "Incorrect number of devices")


if __name__ == '__main__':
    unittest.main()
