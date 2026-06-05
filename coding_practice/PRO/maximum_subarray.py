"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

"""

def max_subarray(nums):
    current_sum = 0
    max_sum = nums[0]

    for i in range(len(nums)):
        current_sum += nums[i]

        if current_sum >= max_sum:
            max_sum = current_sum

        if current_sum < 0:   ## This will catch if the sum goes to -ve
            current_sum = 0

    return max_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
print(max_subarray([5,4,-1,7,8]))