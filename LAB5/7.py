# 7.Write a python program to convert snake case string to camel case string.

import re

def snake_to_camel(snake_str):
    words = snake_str.split('_')
    camel_case = ''.join(word.capitalize() for word in words)
    return camel_case

snake_case_string = "hello_world_example"
camel_case_string = snake_to_camel(snake_case_string)
print(camel_case_string)

