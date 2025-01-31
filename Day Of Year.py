def dayOfYear(date):
    no_leap_year_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year, month, day = map(int, date.split('-'))
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    days_in_months = leap_year_days if is_leap_year else no_leap_year_days
    day_of_year = sum(days_in_months[:month - 1]) + day
    return day_of_year
date = input("Enter the date in year,month,date:")
print(dayOfYear(date))
