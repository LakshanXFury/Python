# Diamond Star Pattern


# Function to print diamond star pattern
def diamond_pattern(rows): # rows = 5
    # Print the top half (including the middle row)
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1)) # (5-1) + (2*1-1) = 4 spaces & 1 star for the 1st iteration

    # Print the bottom half (excluding the middle row)
    for i in range(rows - 1, 0, -1): #rows = 5, so range(rows - 1, 0, -1) → range(4, 0, -1) → Iterates with i = 4, 3, 2, 1.
        print(" " * (rows - i) + "*" * (2 * i - 1))  #(5-4) + (2*4-1) = 1 space & 7 stars for the 1st iteration


# Input number of rows for the top half of the diamond
row = int(input("Enter the number of rows: "))
diamond_pattern(row)
