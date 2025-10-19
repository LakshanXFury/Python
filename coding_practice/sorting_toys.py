"""
Tom and Jerry decide to buy some toys with the money they have. All the toys are different, but their cost can be the
same. Tom only buys the toys whose cost is even, and Jerry buys the toys whose cost is odd.
Find the maximum number of toys Tom and Jerry can buy, respectively.
"""


def toys(val_1: list, val_2: list):
    number_of_toys = val_1[0]
    tom_money = val_1[1]
    jerry_money = val_1[2]

    if len(val_2) != number_of_toys:
        print("Error: The number of toy prices does not match N")
        return

    tom = [i for i in val_2 if i % 2 == 0]
    jerry = [i for i in val_2 if i % 2 != 0]
    # list comprehension automatically handles the “append” for you under the hood.
    # for i in val_2:
    #     if i % 2 == 0:
    #         tom.append(i)
    #     else:
    #         jerry.append(i)

    tom.sort()
    jerry.sort()

    # Buy until money runs out:
    tom_count = jerry_count = 0
    for each_toy in tom:
        if tom_money >= each_toy:
            tom_money -= each_toy
            tom_count += 1
        else:
            break

    for each_toy in jerry:
        if jerry_money >= each_toy:
            jerry_money -= each_toy
            jerry_count += 1
        else:
            break

    print(f"Tom can buy {tom_count} toys \n"
          f"Jerry can buy {jerry_count} toys")


toys(val_1=[10, 54, 75], val_2=[12, 34, 25, 32, 10, 15, 20, 39, 29, 30])
