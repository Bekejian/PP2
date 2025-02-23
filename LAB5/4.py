# 4.Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re
pattern=r"[A-Z][a-z]+$"
texts = ["Pythonn","oBaqzhan","aNurlybek","DiAS","MEREKE","DIORss",'MereKeK']
for text in texts:
    print (f"{text}: {bool(re.search(pattern,text))}")


