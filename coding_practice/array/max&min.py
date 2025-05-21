arr = [8, 2, 5, 1, 9]

# When searching for the min or max of a list, always initialize using the first element of the list, like this:

max_no = arr[0]
min_no = arr[0]

for i in arr:
    if i > max_no:
        max_no = i

    if i < min_no:
        min_no = i


print(min_no)
print(max_no)
