def add(a : float, b : float)->float:
    return a + b

def subtract(a : float, b : float)->float:
    return a - b

def multiply(a : float, b : float)->float:
    return a * b

def divided(a : float, b : float)->float:
    if b == 0:
        raise ValueError("cannot divided by zero")
    return a/b
