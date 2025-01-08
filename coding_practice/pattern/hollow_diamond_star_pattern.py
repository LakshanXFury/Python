def hollow_diamond(rows):
    # Top half of the hollow diamond
    for i in range(1, rows + 1):
        # Print leading spaces
        print(" " * (rows - i), end="")
        if i == 1:
            # Top-most point (single star)
            print("*")
        else:
            # Stars with spaces in between
            print("*" + " " * (2 * i - 3) + "*")  # 2 * 2 - 3 = 1, So 1 space between 2 stars

    # Bottom half of the hollow diamond
    for i in range(rows - 1, 0, -1): # rows-1 = 9, So it is 9 to 0
        # Print leading spaces
        print(" " * (rows - i), end="") # 10-9 =
        if i == 1:
            # Bottom-most point (single star)
            print("*")
        else:
            # Stars with spaces in between
            print("*" + " " * (2 * i - 3) + "*")  # 2*9-3 = 15


# Input from the user
number = int(input("Enter the number of rows for the diamond: "))
hollow_diamond(number)
