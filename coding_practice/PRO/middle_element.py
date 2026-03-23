"""
Finding the middle element in a list
"""

def middle_element(arr):
    slow = 0
    fast = 0

    while fast < len(arr) and fast + 1 < len(arr): # “Is there at least one more step ahead?”
        slow += 1
        fast += 2
        # print(slow, fast)

    return arr[slow]

list1 = [1, 2, 3, 4, 5, 20, 7, 8, 9, 10]
print(middle_element(list1))

list2 = [20, 31, 41, 50, 60, 70]
print(middle_element(list2))

'''
Break it into two parts
1️⃣ fast < len(arr)

👉 Means:

“Is current position valid?”

Example:
If fast = 8 and length = 10 → ✅ OK
If fast = 10 → ❌ out of range

2️⃣ fast + 1 < len(arr)

👉 Means:

“Is there at least one more step ahead?”

Why?

Because to move 2 steps:
You need fast and fast + 1 to exist'''
