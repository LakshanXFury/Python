"""
Write a code to replace each element in an array by its rank in the array
"""

def change_arr(array_list):
    sorted_array = sorted(array_list)
    a = {}
    final_ranks = []
    rank = 0
    for i in sorted_array:
        if i not in a:
            rank += 1 # Increment FIRST
            a[i] = rank

    for arr in array_list:
        # final_ranks[arr] = a.get(arr)
        final_ranks.append(a.get(arr))  # .append() modifies the list in place and returns None

    return final_ranks


print(change_arr([100, 50, 75, 25]))
