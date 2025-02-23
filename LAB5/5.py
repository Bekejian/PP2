# 5.Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re 
pattern=r'a.*b$'
texts=['baga',"baqzhanb",'a3298ybidb','askat','pythonaba','bagashelby','magashelb','zheli']
for text in texts:
    print (f"{text}: {bool(re.search(pattern,text))}")
