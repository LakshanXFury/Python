l1 = [1, 2, 3, 4, 5]
l2 = [5, 10, 15, 20, 25]

l3 = list(map(lambda x, y: x * y, l1, l2))

print(l3)