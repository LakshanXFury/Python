# Write a program to remove duplicates from a list.

list_with_duplicates = [1, 2, 3, 2, 4, 5, 6, 3, 7, 5]

# Using set - Set stores only unique

# unique_list = list(set(list_with_duplicates))
# print(unique_list)


unique_list = []
for item in list_with_duplicates:
    if item not in unique_list:
        unique_list.append(item)


print(unique_list)