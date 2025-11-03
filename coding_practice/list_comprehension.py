"""
Given a list of integers, return a new list containing only the numbers that are divisible by 3 but not divisible by 5.
"""

integer_list = [3, 5, 6, 10, 12, 15, 18, 20]


new_list = [value for value in integer_list if value % 3 == 0 and value % 5 != 0]
print(new_list)
