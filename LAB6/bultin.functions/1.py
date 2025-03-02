# 1.Write a Python program with builtin function to multiply all the numbers in a list\

import math

def multiply_list(numbers):
    return math.prod(numbers)

L=list(map(int, input().split()))
result = multiply_list(L)
print("Product of numbers:", result)