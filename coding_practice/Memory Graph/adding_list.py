a = [1]
b = a # Here B points to same list of A not a copy
b += [2]
b.append(3)
b = [4] # Creates a new list and makes `b` point to it
b.append(5)

print(a)
print(b)