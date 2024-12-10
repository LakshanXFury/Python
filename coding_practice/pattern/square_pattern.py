number = int(input("Enter the number u want to print: "))
"""
****
****
****
****
"""


def pattern(num):
    for i in range(num):  #Outerloop
        for i in range(num): #Innerloop
            print("*", end="")
        print()  # Goes to next line


pattern(number)
