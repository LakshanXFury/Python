# Conversion of two list into Dictionary Using Python


list1 = ["Naina", "kimi", "Sheena"]
list2 = [852345, 763567, 91276]


def list_to_dict(value_a, value_b):
    dictionary = dict(zip(value_a, value_b))   #dictfn will convert into Dictionary
    print(dictionary)


list_to_dict(list1, list2)


def dict_to_tuple():
    x = {'Naina': 852345, 'kimi': 763567, 'Sheena': 91276}
    for i in x.items():  # .items() converts the dictionary into Tuple pairs
        print(i)


dict_to_tuple()

# list1 = ["Naina", "Kimi", "Sheena"]
# list2 = [852345, 763567, 91276]
#
# # Initialize an empty dictionary
# dictionary = {}
#
# # Use a for loop to populate the dictionary
# for i in range(len(list1)):
#     dictionary[list1[i]] = list2[i]
#
# print(dictionary)
