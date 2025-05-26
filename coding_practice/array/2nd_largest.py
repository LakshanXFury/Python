def find_second_largest(arr):
    if len(arr) < 2:
        return "Array must have at least two elements."

    largest = second_largest = float('-inf')  # means negative infinity.

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return "There is no second largest (all elements may be equal)."

    return second_largest



# Example usage
arr = [10, 5, 20, 8, 20]
print("Second largest number is:", find_second_largest(arr))
