"""
Write a function that reads integers from a file and returns their sum. Handle possible exceptions like FileNotFound
    Error and ValueError.
"""

value = 0

try:
    with open(file="number.txt") as file:
        values = file.readlines()
        for num in values:
            try:
                value += int(num.strip())
            except ValueError:
                print(f"{num} is a {type(num)}, so cannot be added")
                continue

except FileNotFoundError:
    print("The file couldn't be found")


print(f"\nThe final Total value is : {value}")
