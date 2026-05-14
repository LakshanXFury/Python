"""
Return True is the number is the power of 2 and Return False otherwise
"""

def power_of_2(num:int):

    # Base Case : Trigger Points
    if num == 0:
        return False
    if num == 1:
        return True
    if num % 2 != 0:
        return False

    # Recursive Case
    return power_of_2(num//2)


print(power_of_2(16))




