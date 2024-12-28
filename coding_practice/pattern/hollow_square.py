## Hollow Square Star Pattern


def hollow_square(rows):
    for i in range(rows):  # Loop through each row
        if i == 0 or i == rows - 1:  # If rows is 0 or is 6 -> It will print 7 stars
            # Print a full row of stars for the top and bottom rows
            print("*" * rows)
        else:
            # Print a hollow row with stars at the boundaries
            print("*" + " " * (rows - 2) + "*")  # (7-2) = 5 , 5 spaces in between


# Input from user
number = int(input("Enter the number of rows: "))
hollow_square(number)
