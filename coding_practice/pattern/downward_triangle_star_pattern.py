""" Downward Triangle Star Pattern """


def downard_pattern(rows):
    for i in range(rows, 0, -1):
        print("*" * i)


input = int(input("Enter the number of Rows that needs to be printed: "))
downard_pattern(input)
