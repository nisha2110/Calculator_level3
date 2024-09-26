from decimal import DivisionByZero

""" Basic arithmetic operations."""
def addition1(a,b):
    """return sum of a and b"""
    return a + b

def subtract1(a,b):
    """return subtract of a and b"""
    return a - b

def multiply(a,b):
     """return mul of a and b"""
     return a * b

def divide(a, b):
    try:
        return a / b
    except DivisionByZero:
        raise ValueError("Cannot divide by zero")
