"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return math.sqrt(a)
    except ValueError as e:
        print(e)
        return None

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError as e:
        print("Both inputs must be numbers.")
        return None
    
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return b / a

def log_base_a(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base 'a' must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Argument 'b' must be positive")
    return math.log(b, a)

def exp(a, b):
    return a ** b

