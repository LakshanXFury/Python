"""
Find Missing Number in a = [1, 3, 5, 4]

"""

a = [1, 3, 5, 4]
n = 5

# Gauss Approach

val = n * (n + 1) // 2
print(val)

sum = 0
for i in a:
    sum += i

print(sum)
print(f"The missing number is {val - sum}")

# XOR Approach
"""
5 in binary:  0101
3 in binary:  0011
             -----
5 ^ 3:        0110  = 6 in decimal
"""

def find_missing_xor(array):
    n = len(array) + 1  # Total numbers including missing one
    result = 0

    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        result ^= i

    # XOR all numbers in the array
    for num in array:
        result ^= num

    return result



print(f"Missing number: {find_missing_xor(a)}")  # 2



