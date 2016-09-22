# coding=UTF8

import random

def is_leap_year():
    year = random.randint(1000, 3000)
    result = ''
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        result = 'Year %s is leap year, have 366 days' %year
        return result
    else:
        result = 'Year %s is regular year, have 365 days' %year
        return result


if __name__ == "__main__":
    print is_leap_year()
