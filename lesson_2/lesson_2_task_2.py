def is_year_leap(year):
    return year % 4 == 0
year = 2023
x = is_year_leap(year)
print("год " + str(year) + ": " + str(x))
