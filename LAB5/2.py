# 2.Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re 
pattern=r"ab{2,3}" 
def search_pattern(s):
  return bool(re.findall(pattern,s)) #search 找到第一个就走了，更省时间
texts=['a','ab','aab','ba','AB','aaaa','abbc','abbb','abba','abbbb','bbbabbb','bab']
for text in texts :
    print(f"{text}: {search_pattern(text)}")

