"""
Count the Digits That Divide a Number
"""

def digits_that_divide_num(num):
    temp = num
    count = 0

    while temp > 0:
        remainder = temp % 10
        if num % remainder == 0:
            count += 1
        temp = temp // 10

    print(count)



digits_that_divide_num(1346)
digits_that_divide_num(1248)
digits_that_divide_num(121)
