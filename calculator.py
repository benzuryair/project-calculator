def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    """multiply 2 numbers"""
    return a * b


def divide(a, b):
    if b == 0:
        return "It is not possible to divide by 0."
    else:
        return a / b
