# 3.Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def is_palindrome(s):
    s=s.lower().replace(" ", "")
    return s == s[::-1]   


text = input()
if is_palindrome(text):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome")