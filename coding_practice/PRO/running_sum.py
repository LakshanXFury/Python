"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]
"""

def running_sum(nums: list) -> list:
    n = len(nums)
    ans = []
    ans.append(nums[0])


    for i in range(1, n):
        x = ans[i-1] + nums[i]
        ans.append(x)

    return ans

print(running_sum([1,2,3,4]))
print(running_sum([3,1,2,10,1]))

