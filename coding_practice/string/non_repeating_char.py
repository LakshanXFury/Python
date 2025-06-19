# Find the first non-repeating character in a string.

def non_char(string):
    s = string.replace(" ", "").lower()  # To remove the spaces

    repeating_char = {

    }

    for i in s:
        # print(i)
        if i not in repeating_char:
            repeating_char[i] = 1
        else:
            repeating_char[i] += 1

    print(repeating_char)
    for i in s:
        if repeating_char[i] == 1:
            print(f"This is the first non-repeating character: {i}")
            break


non_char("lakshan")
