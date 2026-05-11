"""
Recursive Fn
"""


def recursive_fn(i , n):
    # Base Case of recursive fn
    if i > n:
        return
    # Recursive Case
    print(i, end=" ")
    recursive_fn(i+1,n)

recursive_fn(1,5)

# Factorial of a number using recursion
def factorial_recursive_fn(n):
    if n == 0:
        return 1

    return n * factorial_recursive_fn(n-1)


print(factorial_recursive_fn(5))
