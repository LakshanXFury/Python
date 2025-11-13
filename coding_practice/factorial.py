# Find the Factorial of a Number
def factorial_num(number):
    value = 0
    for i in range(int(number), 0, -1):
        if value == 0:
            value = i
        else:
            value = value * i

    print(f"The factorial of the given number {number} is {value}")
    return value


factorial_num(5)
factorial_num(6)

# Using While loop

# def fact(number):
#     result = 1
#     while number >= 1:
#         result = result * number
#         number = number - 1
#     return result
#
#
# print(fact(5))
