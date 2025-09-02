"""
Count the frequency of each character in a string
"""


def frequency(string_value):
    string = string_value.replace(" ", "").lower()
    repeating_char = {

    }

    for i in string:
        if i not in repeating_char:
            repeating_char[i] = 1
        else:
            repeating_char[i] += 1

    print(repeating_char)

    for char in repeating_char:
        print(f"{char} is repeating {repeating_char[char]} times")


string_input = input(str("Enter the String for which you want to check the frequency of ???: "))
frequency(string_input)