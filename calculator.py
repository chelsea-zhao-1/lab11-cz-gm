import math
def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

def mul(a, b): 
    return a * b

def div(a, b): 
    c = b / a
    if a == 0:
        raise ZeroDivisionError
    return c

def log(a, b): 
    c = math.log(b, a)
    if (a < 2) or (b < 1):
        raise ValueError

def exp(a, b): 
    return a**b


