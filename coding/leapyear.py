def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# TODO: Add more code here 👇
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   #stored in a list
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter the year..."))  # Enter a year
month = int(input("Enter the month..."))  # Enter a month
days = days_in_month(year, month)
print(days)