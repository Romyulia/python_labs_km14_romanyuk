import numpy as np
years = list(np.arange(1900, 2020+3, 1))

def leap_year(mha):
    leap_year1 = list(filter(lambda i: i % 400 == 0, mha))
    for i in range(len(leap_year1)):
        mha.remove(leap_year1[i])
    not_a_leap_years = list(filter(lambda i: i % 100 == 0, mha))
    for i in range(len(not_a_leap_years)):
        mha.remove(not_a_leap_years[i])
    leap_year2 = list(filter(lambda i: i % 4 == 0, mha))
    leap_years = leap_year1 + leap_year2
    return leap_years

def days(func, y, m):
    checking = func(years)
    m = str(m)
    if y in checking:
        monthes = {'1': '31',
                   '2': '29',
                   '3': '31',
                   '4': '30',
                   '5': '31',
                   '6': '30',
                   '7': '31',
                   '8': '31',
                   '9': '30',
                   '10': '31',
                   '11': '30',
                   '12': '31'}
        day = monthes.get(m)
    else:
        monthes = {'1': '31',
                   '2': '28',
                   '3': '31',
                   '4': '30',
                   '5': '31',
                   '6': '30',
                   '7': '31',
                   '8': '31',
                   '9': '30',
                   '10': '31',
                   '11': '30',
                   '12': '31'}
        day = monthes.get(m)
    return day

year = input('Enter the year between 1900-2022: ')
while type(year) != int:
    try:
        year = int(year)
        if year > 2022 or year < 1900:
            year = input('Enter the year between 1900-2022: ')
    except Exception:
        year = input('Enter the year between 1900-2022: ')

month = input('Enter the month number (1-12): ')
while type(month) != int:
    try:
        month = int(month)
        if month > 12 or month < 1:
            month = input('Enter the month number (1-12): ')
    except Exception:
        month = input('Enter the month number (1-12): ')

print('Number of days in', month, 'month of', year, 'is', days(leap_year, year, month))