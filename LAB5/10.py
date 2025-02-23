# 10.Write a Python program to convert a given camel case string to snake case

import re

def camel_to_snake(camel_str):
    words = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower().split('_')
    snake_case = '_'.join(words)
    return snake_case

camel_case_string = "HelloWorldExample"
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)