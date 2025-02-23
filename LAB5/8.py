# 8.Write a Python program to split a string at uppercase letters.

import re

def spliter(s):
    return re.findall(r'[A-Z][^A-Z]*', s)  # [^A-Z]*: here the '^' inside the brackets means "not"
text= "Hello@WorldMyNameIsBaqzhan"
print(spliter(text))
