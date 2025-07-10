"""
The outer function (lowercase_decorator) is the decorator itself. It takes a function as an argument.
The inner function (wrapper) is what actually replaces the original function. It adds extra behavior (like converting to lowercase) before or after calling the original function.
This structure allows the decorator to wrap the original function with additional logic.

return string_lowercase (inside wrapper):
This returns the final result after modifying the output of the original function.

return wrapper (inside lowercase_decorator):
This returns the new function (the wrapper) that will replace the original function.

So, both are necessary:
One returns the result of the decorated function.
The other returns the decorated function itself.
"""


def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        return string_lowercase

    return wrapper


def splitter_decorator(function):
    def wrapper():
        func = function()
        string_split = func.split()
        return string_split

    return wrapper


@splitter_decorator
@lowercase_decorator
def hello():
    return "Hello World"


print(hello())
