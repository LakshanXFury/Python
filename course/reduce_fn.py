from functools import reduce

# Find the Sum of first 100 numbers

result = reduce(lambda x, y: x+y, range(1, 101))
print(result)