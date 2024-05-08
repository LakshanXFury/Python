firstnum = input("Enter the first number: ")
secondnum = input("Enter the second number: ")

temp = firstnum
firstnum = secondnum
secondnum = temp

print("The value of first number after swapping is:{} ".format(firstnum))
print("The value of second number after swapping is:{} ".format(secondnum))