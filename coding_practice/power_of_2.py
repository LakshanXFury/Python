"""
Question: Minimum Number to Add to Reach a Power of 2

Problem Statement:

You are given a number X (which is not a power of 2).
You need to find the minimum number that must be added to X so that the result becomes a power of 2.

Definitions:

A power of 2 is a number that can be written as
2
𝑘
2
k
, where
𝑘
k is a non-negative integer.

Examples: 1, 2, 4, 8, 16, 32, …

Input:

A single integer X.

Output:

A single integer, which is the minimum number to add to X to make it a power of 2.

Example:

Input	Output	Explanation
12	4	Next power of 2 ≥ 12 is 16 → 16 - 12 = 4
20	12	Next power of 2 ≥ 20 is 32 → 32 - 20 = 12
7	1	Next power of 2 ≥ 7 is 8 → 8 - 7 = 1
"""


def power_of_2(number: int):
    value = 1

    while value < number:
        value = value * 2
        # print(value)

    return f"The value is: {value - number}"


print(power_of_2(20))
print(power_of_2(12))