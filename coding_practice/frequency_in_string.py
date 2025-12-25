"""
Write code to Calculate frequency of words in a string
"""

def frequency(string:str):
    lower_string = string.lower()
    split_string = lower_string.split()

    a = {}
    for i in split_string:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1

    print(a)

string_val = str(input("Enter the string : "))
frequency(string_val)

