"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""


# This is using 3 pointer Approach

def sort_colors(nums):
    left = 0
    right = len(nums)-1
    print(right)
    i = 0

    while i <= right:
        if nums[i] == 1:
            i += 1
        elif nums[i] == 0:
            temp = nums[i]
            nums[i] = nums[left]
            nums[left] = temp
            i += 1
            left += 1
        else:
            temp = nums[i]
            nums[i] = nums[right]
            nums[right] = temp
            right -= 1

    return nums

print(sort_colors([2,0, 2, 1, 1, 0]))
