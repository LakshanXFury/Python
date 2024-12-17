# Pyramid Star Pattern

# Function to print pyramid star pattern
def pyramid_pattern(rows):
    for i in range(1, rows + 1):
        # Print spaces
        print(" " * (rows - i), end="")  # For example, if rows = 5 and i = 1, (5 - 1) = 4 spaces will be printed.
        # Print stars
        print("*" * (2 * i - 1))  # If i = 1, stars = 1 (2 * 1 - 1)


# Input number of rows for the pyramid
rows = int(input("Enter the number of rows: "))
pyramid_pattern(rows)

