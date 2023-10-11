"""
Scope
1. local
2. global
"""

# global scope
c = 50


def summation():
    a = 20  # local scope
    b = 50
    print(a + b + c)


def subtraction():
    a = 20
    b = 5
    print(a - b - c)


summation()
subtraction()


