"""
Write a code to find non-repeating elements in an array.
"""

def non_repeating_char(array_list):
    a = {}
    for element in array_list:
        if element in a:
            a[element] += 1
        else:
            a[element] = 1

    for key, value in a.items(): # .items() returns all key-value pairs from a dictionary as tuples.
        if value == 1:
            print(f"The character {key} is a non-repeating character")


non_repeating_char([1, 2, 3, 2, 4, 1, 5])

