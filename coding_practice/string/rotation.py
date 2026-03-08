"""
Check if the one string is the rotation of the other string or not ?
"""

def rotation(str1, str2):
    if len(str1) != len(str2):
        return False

    string1 = str1 + str1
    print(string1)
    if str2 in string1:
        return True

    return False



s1 = "waterbottle"
s2 = "erbottlewat"
print(rotation(s1, s2))