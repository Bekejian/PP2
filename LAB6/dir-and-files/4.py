import os
print("FOURTH TASK")
import string

with open("file2.txt") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
f.close()