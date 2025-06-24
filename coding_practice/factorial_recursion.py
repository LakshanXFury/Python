"""
Find the Factorial of a Number using recursion
"""


def factorial_recursion(n):
    print("Executing Factorial Fn with n vlaue: ", n)
    if n == 0:
        result = 1
    else:
        result = n * factorial_recursion(n-1)
    print("Returning Factorial ({}) is {}".format(n, result))
    return result


print(factorial_recursion(4))