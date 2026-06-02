"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k.
After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order.
The remaining elements beyond index k - 1 can be ignored.
"""

def remove_duplicates(nums):
    n = len(nums)
    start = 0

    # it follows 2 pointer approach  :
    # nums[i]     = nums[2] = 2
    # nums[start] = nums[0] = 1
    # 2 != 1  → NEW element found! -> nums[1] = 2 -> nums: [ 1, 2, 2 ]

    # 4 != 3 → NEW! start++ → start=4, nums[4] = 4

    for i in range(1, n):
        if nums[i] != nums[start]:
            start += 1
            nums[start] = nums[i]

    print(nums)
    print(start+1)
    print("\n")


remove_duplicates(nums = [0,0,1,1,1,2,2,3,3,4])
remove_duplicates(nums = [1,1,2])