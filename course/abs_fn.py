"""
abs() : Turn any negative number into positive — but keep positive numbers as they are.

"""


def myfunc(n):
    return abs(10 - n)


a = (5, 3, 1, 11, 2, 12, 17)
x = sorted(a, key=myfunc)
print(x)
