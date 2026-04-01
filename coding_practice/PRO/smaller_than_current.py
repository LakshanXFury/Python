"""
How many numbers are smaller than the current number?
"""


def smaller_than_current(n:list[int]):
    final_list = []
    for i in n:
        count = 0
        for j in n:
            if j < i:
                count += 1

        final_list.append(count)
    print(final_list)




smaller_than_current([8, 1, 1, 7 , 4])