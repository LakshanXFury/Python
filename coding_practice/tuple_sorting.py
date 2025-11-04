"""
Given a list of tuples like [(name, age), ...], sort it by age descending and then by name ascending.

"""


# A lambda function can take any number of arguments, but can only have one expression.

def tuple_sorting(list_with_data):
    # Sorting age in descending order and Name in Ascending Order
    sorted_descending_order = sorted(list_with_data, key=lambda x: (-x[1], x[0]))
    print(sorted_descending_order)

    """
    👉 Explanation:
    -x[1] → sorts age descending (reverse)
    x[0] → sorts name ascending when ages are the same                                      
    """


tuple_sorting([("David", 35), ("Bob", 30), ("Alice", 25), ("Charlie", 25)])
