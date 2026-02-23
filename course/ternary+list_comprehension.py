"""
List comprehension with a conditional expression (ternary operator)
"""

a = [1 if i%2 else 0 for i in range(6)]
print(a)

"""
Falsy values (evaluate to False):

0 (zero)
"" (empty string)
[] (empty list)
None
False

Truthy values (evaluate to True):

Any non-zero number (1, 2, -5, etc.)
Any non-empty string ("hello", "a")
Any non-empty container ([1], [2,3])
True

i = 0:
  i % 2 = 0  (even, falsy)
  1 if 0 else 0 → 0

i = 1:
  i % 2 = 1  (odd, truthy)
  1 if 1 else 0 → 1

i = 2:
  i % 2 = 0  (even, falsy)
  1 if 0 else 0 → 0

i = 3:
  i % 2 = 1  (odd, truthy)
  1 if 1 else 0 → 1

i = 4:
  i % 2 = 0  (even, falsy)
  1 if 0 else 0 → 0

i = 5:
  i % 2 = 1  (odd, truthy)
  1 if 1 else 0 → 1
  """