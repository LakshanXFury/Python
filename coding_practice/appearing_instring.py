# Count the frequency of words appearing in a string Using Python

#The little bird kept chirping, chirping, and chirping as it flew over the bright, blue sky, enjoying the fresh breeze and the warmth of the glowing, glowing sun.
def appearing():
    string = input("Enter a sentence: ").lower()
    li = string.split()
    print(li)
    d = {}

    for i in li:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i] + 1
    print(d)



appearing()