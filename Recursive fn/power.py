"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
"""
def find_power(x, n):
    if n == 0:
        return 1
    a = find_power(x, n//2)

## even → a × a          (nothing lost in halving)
# odd  → a × a × x      (one x lost when flooring, add it back)
    if n % 2 == 0:
        return a * a
    else:
        return a * a * x


def power(x, n):
    if n >=0:
        return find_power(x,n)
    else:
        return 1/find_power(x,n*(-1)) # A negative exponent means how many times do you divide 1 by that number.


print(power(2, 10))
print(power(3, 8))
print(power(2, -3))