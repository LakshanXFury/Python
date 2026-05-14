"""
Tribonacci Number

This is using the recursion tree for performing this operation : tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
"""

def tribonacci(n):

    # Base Case
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    # Recursive Case
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


print(tribonacci(10))