def butterfly_pattern(rows):
    # Top half of the butterfly
    for i in range(1, rows + 1):
        # Left stars
        print("*" * i, end="")
        # Spaces in the middle
        print(" " * (2 * (rows - i)), end="")
        # Right stars
        print("*" * i)

    # Bottom half of the butterfly
    for i in range(rows, 0, -1): # For rows = 4, it will iterate with i = 4, 3, 2, 1.
        # Left stars
        print("*" * i, end="")
        # Spaces in the middle
        print(" " * (2 * (rows - i)), end="")
        # Right stars
        print("*" * i)

# Input from user
number = int(input("Enter the number of rows: "))
butterfly_pattern(number)
