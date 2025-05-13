"""
Till the condition is TRUE it will keep executing and will stop once it is FALSE
"""

name = input("Enter your name ")

while name == "":
    print("Name cannot be empty")
    name = input("Enter your name ")

age = int(input("Enter your age "))

while age < 5:
    print("Age cant be less than 5")
    age = int(input("Enter your age "))


print(f"Your name is: {name}")
print(f"Your age is: {age}")