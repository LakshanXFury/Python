"""
Shallow and Deep Copy
"""


import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)        # shallow copy (same as a[:], list(a), a.copy())

print(a is b)           # False (new outer list)
print(a[0] is b[0])     # True  (inner lists are the same objects)

b[0].append(99)
print(a)  # [[1, 2, 99], [3, 4]]   <-- a changed because inner list is shared
print(b)  # [[1, 2, 99], [3, 4]]


# Deep Copy ---------------------------------------------------------------------------------------------------------

a = [[1, 2], [3, 4]]
c = copy.deepcopy(a)

print(a is c)           # False
print(a[0] is c[0])     # False (inner lists are also new)

c[0].append(99)
print(a)  # [[1, 2], [3, 4]]        <-- no change
print(c)  # [[1, 2, 99], [3, 4]]
