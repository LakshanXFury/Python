"""
The slot machine project
"""

import random

slot_values = ["Cherry", "Lemon", "Bell", "Seven", "Bar"]

print("Welcome to slot machine project\n")

coins = int(input("Enter the coins that you have: "))

while coins > 0:
    slotted = []
    input_val = input("Type SLOT to run: ").lower()
    coins -= 1
    if input_val == "slot":
        for _ in range(3):  # _ means: “I am looping, but I don’t care about the index.”
            slotted.append(random.choice(slot_values))
        joined = " | ".join(slotted)  # combines all elements of the list into one string, separated by |.
        print(joined)
        print(f"Coins left: {coins}\n")
    else:
        print("Type SLOT to run !!!")
print("Oops! You are out of coins.")