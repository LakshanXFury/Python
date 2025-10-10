"""
Count the number of 1-bits in a number.
"""


def bits(num):
    val = 0
    while num > 0:
        result = num & 1  # checks if the last value in 0 or 1
        if result == 1:
            val += 1
        num = num >> 1  # Removes the last value and keeps the left values

    print(val)


bits(10)
bits(7)
