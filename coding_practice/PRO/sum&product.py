"""
Subtract the Product and Sum of Digits of an Integer
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Example 1:

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
"""


def subtractproductndsum(n: int) -> int:
    product_of_digits = 1
    sum_of_digits = 0

    while n > 0:
        i = n % 10
        product_of_digits *= i
        sum_of_digits += i
        n //= 10

    print("Sum of digits: " + str(sum_of_digits))
    print("Product of digits: " + str(product_of_digits))

    return product_of_digits - sum_of_digits

print(subtractproductndsum(299))