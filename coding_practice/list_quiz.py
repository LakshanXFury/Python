"""The for loop's iterator moves to the next index in the original list, which was index 1 (20).
However, because 10 was removed, 20 has shifted to index 0, and the loop skips it and moves directly to index 1 (30)."""


a = [10,20,30,40,50]

for i in a:
    a.remove(i)
print(a)