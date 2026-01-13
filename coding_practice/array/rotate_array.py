"""
Code to find circular rotation of an array by K positions
"""


def rotate_array(array, k_value):
    n = len(array)
    k_value = k_value % n  # handle k greater than array size
    # print(k_value)
    return array[-k_value:] + array[:-k_value]


# array[-2:] → [40, 50]  # last k elements using Slicing
# # array[:-2] → [10, 20, 30]  # all except last k


# Example usage:
arr = [10, 20, 30, 40, 50]
k = 2
rotated = rotate_array(arr, k)
print(rotated)  # Output: [40, 50, 10, 20, 30]

# --------------------------------------- #
# value = 2 % 5
# print(value)

# arr = [10, 20, 30, 40, 50]
#
# first = arr[-2:]
# second = arr[:-2]
# print(first+second)
