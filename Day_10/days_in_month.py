days=[31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap_year(year):
    leap = year % 4 == 0
    leap = leap and (year % 100 != 0 or year % 400 == 0)
    return leap

def days_in_months(year, month):
    if month == 2 and is_leap_year(year):
        return 29
    else:
        return days[month-1]
    

year=int(input("enter the year: "))
month=int(input("enter the month: "))
print(f"{days_in_months(year,month)}")