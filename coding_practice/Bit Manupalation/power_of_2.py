"""
Check if a number is a power of 2.
| Number | Can it be made by multiplying 2s? | Explanation                     |
| ------ | --------------------------------- | ------------------------------- |
| 1      | ✅ Yes                             | (2^0 = 1)                       |
| 2      | ✅ Yes                             | (2^1 = 2)                       |
| 4      | ✅ Yes                             | (2^2 = 4)                       |
| 8      | ✅ Yes                             | (2 × 2 × 2 = 8)                 |
| 16     | ✅ Yes                             | (2 × 2 × 2 × 2 = 16)            |
| 6      | ❌ No                              | Can’t be made by multiplying 2s |
| 10     | ❌ No                              | Not made by 2s only             |

So basically,
👉 if a number can be written as 2 × 2 × 2 × … (some number of times) → it is a power of 2.
👉 if not → it is not a power of 2.
"""


def if_power_of_2(num):
    if num <= 0:
        print(f"{num} can’t be a power of 2 (powers of 2 are always positive).")
        return

    while num > 1:
        if num % 2 != 0:  # Takes the reminder
            print(f"{num} is not a power of 2.")
            return
        num = num // 2  # Takes the quotient
        print(num)

    print("It is a power of 2!")


if_power_of_2(8)
