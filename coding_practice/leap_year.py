"""
Write to code to check whether a given year is leap year or not

Year 1896: 4✓, 100✗, 400✗ → Leap year (divisible by 4)
Year 1900: 4✓, 100✓, 400✗ → NOT leap year (century, not divisible by 400)
Year 1904: 4✓, 100✗, 400✗ → Leap year (divisible by 4)
Year 2000: 4✓, 100✓, 400✓ → Leap year (divisible by 400)
Year 2004: 4✓, 100✗, 400✗ → Leap year (divisible by 4)
Year 2100: 4✓, 100✓, 400✗ → NOT leap year (century, not divisible by 400)

"""

def leap_year(year:int):

    if year % 400 == 0:
        print("It is a leap year")
    else:
        if year % 100 == 0:
            print("It is not a leap year.")
        else:
            if year % 4 == 0:
                print("It is a leap year")
            else:
                print("It is not a leap year.")

year = int(input("Type the year that you want to check as Leap Year ? :"))
leap_year(year)

"""
Logic 

Why divide by 100?

Adding a day every 4 years overcompensates slightly
To fix this, we skip leap years on century years (1700, 1800, 1900, 2100)
Rule: Years divisible by 100 are NOT leap years (exception to the rule of 4)

Why divide by 4?

0.25 days × 4 years = 1 extra day
So every 4 years, we add one day to catch up
Rule: Years divisible by 4 are leap years

Why divide by 400?

To fine-tune even more, we make century years divisible by 400 back into leap years
Rule: Years divisible by 400 ARE leap years (exception to the exception)

Imp :
100 rule: Removes most century years from being leap years
400 rule: Adds back certain century years (every 400 years) to be leap years
"""