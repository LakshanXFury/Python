""" Downward Triangle Star Pattern """


def downard_pattern(rows):
    for i in range(rows, 0, -1):
        print("*" * i)


downard_pattern(10)
