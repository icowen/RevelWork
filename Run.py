import unittest
import warnings

from GetRevelData import GetRevelData

warnings.simplefilter(action='ignore', category=FutureWarning)


class MyTestCase(unittest.TestCase):
    def test_GET_DATA(self):
        start = '2/24/2020'     # dates for week 8
        end = '2/28/2020'
        filename = 'data/cet/2020Week8.xlsx'
        report = GetRevelData(start, end, filename)
        self.assertIsNotNone(report.revel_df)


if __name__ == '__main__':
    unittest.main()
