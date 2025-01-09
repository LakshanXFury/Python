def left_pascal(rows):
    for i in range(rows + 1):
        print("*" * i)

    for i in range(rows - 1, 0, -1): # 4,3,2,1
        print("*" * i)


row = int(input("Enter the number of rows "))
left_pascal(row)
