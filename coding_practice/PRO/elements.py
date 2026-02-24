"""
Re-arrange elements by sign
"""

a = [45, -45, 60, -75, -11, 15, 20, -25, 30, -35, 20, 10, 50]

final_list = []

positive_list = []
negative_list = []

for i in a:
    if i > 0:
        positive_list.append(i)
    if i < 0:
        negative_list.append(i)

# print(positive_list)
# print(negative_list)

for pos , neg in zip(positive_list, negative_list):
    final_list.append(pos)
    final_list.append(neg)

# list slicing - it takes elements starting from index 5 to the end.
final_list.extend(positive_list[len(negative_list):])

print(final_list)

""" Two Pointer Approach"""
pos_index = 0  # Pointer for positive list
neg_index = 0  # Pointer for negative list

pointer_final_list = []

# While both pointers are within their lists
while pos_index < len(positive_list) and neg_index < len(negative_list):
    pointer_final_list.append(positive_list[pos_index])
    pos_index += 1  # Move positive pointer forward

    pointer_final_list.append(negative_list[neg_index])
    neg_index += 1  # Move negative pointer forward

# Add remaining positives (if any)
while pos_index < len(positive_list):
    pointer_final_list.append(positive_list[pos_index])
    pos_index += 1

# Add remaining negatives (if any)
while neg_index < len(negative_list):
    pointer_final_list.append(negative_list[neg_index])
    neg_index += 1

print(f"The 2 pointer approach list is{pointer_final_list}")


