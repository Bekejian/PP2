# 6.Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re 
text="Hello,Baqzhan! I wish you could learn the Python really well !"
text2=input()
result=re.sub('[ ,.]',':',text)
result2=re.sub('[ ,.]',':',text2)
print(result,result2,sep='\n')

