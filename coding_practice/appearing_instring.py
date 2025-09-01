# Count the frequency of words appearing in a string Using Python

# The little bird kept chirping, chirping, and chirping as it flew over the bright, blue sky, enjoying the fresh
# breeze and the warmth of the glowing, glowing sun.
def appearing(string):
    li = string.split()
    print(li)
    d = {}

    for i in li:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    print(d)


string_input = input("Enter a sentence: ").lower()
appearing(string_input)
