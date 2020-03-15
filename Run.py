import unittest
import warnings

from GetRevelData import GetRevelData

warnings.simplefilter(action='ignore', category=FutureWarning)


class MyTestCase(unittest.TestCase):
    def test_GET_DATA(self):
        start = '2/1/2020'
        end = '2/7/2020'
        filename = 'data/cet/2020Week8.xlsx'
        report = GetRevelData(start, end, filename)
        self.assertIsNotNone(report.revel_df)


if __name__ == '__main__':
    unittest.main()
