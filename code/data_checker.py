'''
Validity checker for the date given by user
'''
from datetime import date

def check_date(date_str):
    '''
    Splits the date string into 3 different parts and
    validates that the year, month, and day are possible
    ad individual values and then together.
    '''
    current_date = date.today()
    current_year = current_date.year

    year, month, day = date_str.split('-')

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    year = int(year)
    if year < 1950 or year > current_year:
        return False

    month = int(month)
    if month < 1 or month > 12:
        return False

    day = int(day)
    if day < 1 or day > 31:
        return False

    if (month in [4, 6, 9, 11] and day > 30) or (month == 2 and day > 28) or day > 31:
        return False

    return True
