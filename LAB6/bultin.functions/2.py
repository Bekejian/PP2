# 2.Write a Python program with builtin function that accepts a string and calculate the number of 
# upper case letters and lower case letters

def count(s):
    up_count = 0
    low_count = 0

    for char in s:
        if char.isupper():
            up_count += 1
        elif char.islower():
            low_count += 1

    return up_count, low_count


text = input()
upper, lower = count(text)

print(upper)
print(lower)