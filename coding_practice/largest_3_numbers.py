num1 = float(input("Enter the First number: "))
num2 = float(input("Enter the Second number: "))
num3 = float(input("Enter the Third number: "))

if (num1 >= num2) and (num1 >= num2):
    largest = num1
elif (num2 >= num3) and (num2 >= num1):
    largest = num2
else:
    largest = num3

print(f"The largest number is: {largest}")