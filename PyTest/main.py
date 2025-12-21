def add(a:int, b:int):
    return a+b

print(add(5, 10))


def get_weather(temp:int):
    if temp > 20:
        return "hot"
    else:
        return "cold"

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b
