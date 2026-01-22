"""
Find the maximum value and minimum value in the list
"""

def max_min(value):
    maxi = mini = value[0]
    for i in value:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i

    print(f"The maximum value in list is: {maxi}")
    print(f"The minimum value in list is: {mini}")




list = [7, 23, 41, 56, 68, 72, 85, 91, 99, 34, 5]
max_min(list)