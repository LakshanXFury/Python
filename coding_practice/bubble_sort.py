"""
Bubble sort
range will start from O
len will start from 1
"""

def bubble_sort(arr_list):
    n = len(arr_list)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr_list[j] > arr_list[j+1]:
                arr_list[j], arr_list[j+1] = arr_list[j+1],  arr_list[j]
                swapped = True

        if not swapped:
            break

    return arr_list

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original:", numbers)
print("Sorted:", bubble_sort(numbers))