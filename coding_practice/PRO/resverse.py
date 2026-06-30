"""
Reverse a string using 2 pointer method
"""

def reverse_string(s):
    s = list(s.lower())   # turns into individual characters

    i = 0
    j = len(s) - 1

    while i < j:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i += 1
        j -= 1

    return s



print(reverse_string("Malayalam"))
print(reverse_string("Lakshan"))