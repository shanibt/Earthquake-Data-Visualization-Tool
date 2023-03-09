# NAME: Shani Trieu
# EMAIL: shanibt@uci.edu
# STUDENT ID: 16539648

def check_date(date_str):
    year, month, day = date_str.split('-')

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    year = int(year)
    if year < 1950 or year > 2023:
        return False

    month = int(month)
    if month < 1 or month > 12:
        return False

    day = int(day)
    if day < 1 or day > 31:
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False
    elif month == 2 and day > 28:
        return False
    elif day > 31:
        return False

    return True
