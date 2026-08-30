"""
An efficient algorithm used to find the position of a target value within a sorted array or list.
It works by repeatedly dividing the search space in half until the target is found or the search space is exhausted
"""
values = [2, 5, 8, 12, 16, 23, 38, 56, 72]


def binary_search(value, target):

    n = len(value)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        # print(mid)
        if target == value[mid]:
            return mid
        elif target > value[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

print(binary_search(values,16 ))
print(binary_search(values,17 ))

print(binary_search(values,72 ))
