"""
Merge all the 1 to the end of the array
"""

a = [1, 1, 2, 3, 1, 4, 5, 1]
# final_list = []
# extend_val = []

# for i in a:
#     if i != 1:
#         final_list.append(i)
#     else:
#         extend_val.append(i)

# Using Concantination and list comprehension
final_list = [i for i in a if i != 1] + [i for i in a if i == 1]

# final_list.extend(extend_val)
print(final_list)