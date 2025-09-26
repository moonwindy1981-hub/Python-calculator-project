"""
====================================================
 Mini Calculator Project - math_core.py
----------------------------------------------------
 Purpose: 
   - Contains all core math functions (add, subtract, multiply, divide, sqrt, power).
   - Designed to be reusable for different UIs.
==================================
"""
import math

def calculate(a, b, op):
    if op == '+': 
        return a + b
    if op == '-': 
        return a - b
    if op == '*': 
        return a * b
    if op == '/':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by 0")
        return a / b
    if op == '^2':
        return a ** 2
    if op == 'sqrt':
        if a < 0:
            raise ValueError("Cannot take sqrt of negative number")
        return math.sqrt(a)
    raise ValueError("Does not support this operator")