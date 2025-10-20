"""
Maximum Sum of GCD Given are two arrays

Take the first element of array A (in order, one by one).

From array B, you can take either the first OR the last element.

Compute the GCD (Greatest Common Divisor) of the two numbers.

Remove the chosen element from B.

Repeat this for every element of A.
"""
import math
from functools import lru_cache


def maxSum(N, A, B):
    @lru_cache(None)
    def helper(i, l, r):
        if i == N:
            return 0
        take_left = math.gcd(A[i], B[l]) + helper(i + 1, l + 1, r)
        take_right = math.gcd(A[i], B[r]) + helper(i + 1, l, r - 1)
        return max(take_left, take_right)

    return helper(0, 0, N - 1)


# INPUT
N = int(input("Enter N: ").strip())
A_input = input("Enter array A: ").strip()
B_input = input("Enter array B: ").strip()

if " " in A_input:
    A = list(map(int, A_input.split()))
    B = list(map(int, B_input.split()))
else:
    A = [int(ch) for ch in A_input]
    B = [int(ch) for ch in B_input]

# OUTPUT
print("Maximum Sum of GCD:", maxSum(N, A, B))


# Input
# Enter N: 3
# Enter array A: 123
# Enter array B: 321
