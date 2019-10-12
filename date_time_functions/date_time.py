"""
Author: Michael Harmon
Date: 10/11/2019
Description: This program will use datetime to calculate
a half birthday
"""
from datetime import datetime, timedelta


def half_birthday(my_birthday):
    """
    calculate half birthday by adding 6 months to date
    :param my_birthday: recent birthday date
    :return: half birthday 6 months later
    """
    pass


if __name__ == '__main__':
    my_recent_birthday = datetime(2018, 11, 19)
    print(half_birthday(my_recent_birthday))
