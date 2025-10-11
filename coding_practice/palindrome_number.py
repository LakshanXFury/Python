"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Follow up: Could you solve it without converting the integer to a string?
"""


def palindrome_num(x: int) -> bool:
    if x <= 0 or (x % 10 == 0 and x != 0):
        #  Negative numbers are not palindromes.
        # Numbers ending in 0 (except 0 itself) cannot be palindromes.
        return False

    reversed_num = 0
    original_val = x

    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x = x // 10

    return reversed_num == original_val


print(palindrome_num(123))
print(palindrome_num(202))

# Why base 10 matters => When you look at a number like 4562, what it really means is:
#
# 4×1000 + 5×100 + 6×10 + 2×1

# Dividing by 10 moves you one digit to the right (drops the last digit).
# Taking modulo 10 gives you the remainder when divided by 10 — which is exactly the last digit.

