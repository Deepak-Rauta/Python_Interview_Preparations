import calendar
def find_day(month, date, year):
    day_of_week = calendar.weekday(year, month, date)
    day_name = calendar.day_name[day_of_week]
    return day_name.upper()
Month = 11
Date = 22
year = 1999
result = find_day(Month, Date, year)
print(result) 




