"""
Find the missing number in the list of array ?
"""


def missing_value(array_list):
    max_val = max(array_list)
    # Using the natural number sum formula
    # n(n+1)/2 => Formula

    expected_sum = max_val * (max_val+1) // 2

    actual_sum = sum(array_list)

    # So if we do expected_sum - actual_sum we get the missing value

    missing = expected_sum - actual_sum
    print(f"The missing value in the array list is : {missing}")


arr = [2, 3, 6, 1, 5, 0]
missing_value(arr)
