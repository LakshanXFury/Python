def right_pascal(num: int):
    for i in range(1, num + 1):
        print(" " * (num - i), end="")
        print("*" * i)

    # Below right triangle
    for j in range(num - 1, 0, -1):
        print(" " * (num - j), end="")
        print("*" * j)


row = int(input("Enter the number of rows: "))
right_pascal(row)
