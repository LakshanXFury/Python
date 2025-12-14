"""
Write code of  Perfect number

A perfect number is a number that is equal to the sum of its proper divisors.
Proper divisors:
Divisors excluding the number itself
They always include 1
They must divide the number exactly
"""


def perfect_number(num):
    proper_divisor_sum = 0

    for i in range(1, num//2 + 1):
        # print(i)
        remainder = num % i
        if remainder == 0:
            proper_divisor_sum += i

    if proper_divisor_sum == num:
        print(f"{num} is the perfect number")
    else:
        print(f"{num} is not the perfect number")


perfect_number(12)
perfect_number(16)
perfect_number(6)