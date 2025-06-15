from sys import argv

# To get the SUM of values passed from Command Line Arguments

args = argv[1:]

total_sum = 0


for i in args:
    total_sum += int(i)

print("The Total sum value is :", total_sum)