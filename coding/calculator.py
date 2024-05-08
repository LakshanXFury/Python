#Add
def add(a, b):
  return a + b
#Subtract
def subtract(a, b):
  return a - b
#Multiply
def multiply(a, b):
  return a * b
#Divide
def divide(a, b):
  return a / b

#Dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}
num1 = int(input("What's the first number?: "))

for symbol in operations:
  print(symbol)
operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number?: "))
#Calculation
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")