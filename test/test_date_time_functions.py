import unittest
import datetime
from date_time_functions import date_time as dt


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        my_recent_birthday = datetime.datetime(2018, 11, 19)
        my_half_birthday = datetime.datetime(2019, 5, 19)
        self.assertEqual(dt.half_birthday(my_recent_birthday), my_half_birthday)


if __name__ == '__main__':
    unittest.main()
