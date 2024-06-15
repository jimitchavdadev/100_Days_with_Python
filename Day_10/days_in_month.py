# List of days in each month (non-leap year)
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Function to check if a year is a leap year
def is_leap_year(year):
    leap = year % 4 == 0  # Leap year if divisible by 4
    leap = leap and (year % 100 != 0 or year % 400 == 0)  # Exclude multiples of 100 unless also multiples of 400
    return leap

# Function to determine the number of days in a specific month of a year
def days_in_months(year, month):
    if month == 2 and is_leap_year(year):  # If February and it's a leap year
        return 29  # February has 29 days in a leap year
    else:
        return days[month - 1]  # Return the number of days for the specified month (index adjusted for 0-based indexing)

year = int(input("Enter the year: "))  # Get the year from the user
month = int(input("Enter the month: "))  # Get the month from the user
print(f"Number of days: {days_in_months(year, month)}")  # Print the number of days for the specified month and year