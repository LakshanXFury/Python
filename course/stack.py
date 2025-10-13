"""
A stack in Python is a linear data structure that follows the Last-In-First-Out (LIFO) principle,
meaning the last element added to the stack is the first one to be removed.
"""

# Create an empty stack
my_stack = []

# Push elements onto the stack
my_stack.append("apple")
my_stack.append("banana")
my_stack.append("cherry")

print(f"Stack after pushes: {my_stack}")

# Peek at the Last element
top_element = my_stack[-1]
print(f"Last element: {top_element}")

# Pop elements from the stack
popped_element = my_stack.pop() # If the index in not specified it pops the last element .
print(f"Popped element: {popped_element}")
print(f"Stack after pop: {my_stack}")

# Check if the stack is empty
if not my_stack:
    print("The stack is empty.")
else:
    print("The stack is not empty.")
# ---------------------------------------------------------------------------------------------------------------------
print("\nCode below to POP every element from the list:")

while my_stack:
    popped_element = my_stack.pop()
    print(f"Popped element: {popped_element}")
    print(f"Stack after pop: {my_stack}")

    if not my_stack:
        print("The stack is finally empty :)")
