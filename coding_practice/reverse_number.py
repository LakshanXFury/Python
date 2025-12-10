"""
Write a code to reverse a number
"""

a = int(input("Enter the number you want to reverse: "))

rev = 0


while a > 0 :
    last_digit = a % 10
    rev = rev * 10 + last_digit
    a = a // 10

print(rev)


"""
Since it is Decimal value , so we use base 10
| Operation      | Why we use 10              | Purpose                   |
| -------------- | -------------------------- | ------------------------- |
| `a % 10`       | Gets last digit in base 10 | Extract rightmost digit   |
| `a // 10`      | Removes last digit         | Shrink number             |
| `rev * 10`     | Shifts digits left         | Makes space for new digit |
| `+ last_digit` | Add new digit              | Build reversed number     |
"""