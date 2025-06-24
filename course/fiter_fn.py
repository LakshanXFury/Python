# To check if the given number is Odd or Even using the filter fn and lambda

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
1. lambda n: n % 2 == 0
    This is an anonymous function (a function without a name).
    It takes one argument n and returns True if n is even (i.e., divisible by 2), otherwise False.
2. filter(function, iterable)
    The filter() function applies the given function to each item in the iterable.
    It keeps only those items for which the function returns True.
"""

l1 = list(filter(lambda n: n % 2 == 0, numbers))
print(l1)
