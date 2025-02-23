# 1.Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re 
pattern=r"ab*" 
def search_pattern(s):
  return bool(re.findall(pattern,s)) 
texts=['a','ab','aab','ba','AB','aaaa','abbc','va','ca','av','ac','bab']
for text in texts :
    print(f"{text}: {search_pattern(text)}")

 