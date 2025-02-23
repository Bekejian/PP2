# 3.Write a Python program to find sequences of lowercase letters joined with a underscore.

import re
pattern=r"[a-z]+_[a-z]+"
texts = ["hello_world", "hello_World", "automation_and_control", "my_name_is_Baqzhan",
         "snake_case", "abc_def_pp2","myhello_world", "test_china123"]
for text in texts:
    print (f"{text}: {bool(re.search(pattern,text))}")


