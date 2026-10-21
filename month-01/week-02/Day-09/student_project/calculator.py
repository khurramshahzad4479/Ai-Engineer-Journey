def add(a : float, b : float)->float:
    return a+b

def subtract(a : float, b : float)->float:
    return a-b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a : float, b : float)->float:
    if b == 0:
        raise ValueError("Not divided by zero")
    return a/b

print(divide(10,2))

try:
    print(divide(10, 0))
except ValueError as e:
    print(e)