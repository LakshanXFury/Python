"""
Write code of Greatest Common Divisor
"""

# def gcd(inta: int, intb: int) -> int:
#
#     def recusrsion(bigger , smaller):
#
#         remainder = bigger % smaller
#
#         if remainder == 0:
#             print(f"The GCD is : {smaller}")
#         else:
#             recusrsion(smaller, remainder)
#             print("Running a recursion")
#
#     smaller_no = 0
#     bigger_no = 0
#
#     if inta != intb:
#         if inta > intb:
#             bigger_no += inta
#             smaller_no += intb
#             # print(f"{inta} Integer A is bigger")
#         elif intb > inta :
#             bigger_no += intb
#             smaller_no += inta
#             # print(f"{intb} Integer B is bigger")
#
#         recusrsion(bigger_no, smaller_no)
#     else:
#         print(f"The GCD is : {inta}")


def gcd(a: int, b: int) -> int:
    # Base case: if one number becomes 0, the other is the GCD
    if b == 0:
        return a
    # Recursive case
    return gcd(b, a % b)

"""
a becomes the previous b
b becomes the remainder
The remainder (b) is the value that shrinks toward 0, not a.
That’s why:
b == 0 means there is nothing left to divide → stop.
"""


print(gcd(9, 18))
print(gcd(48, 18))
print(gcd(10, 10))
print(gcd(0, 5))
