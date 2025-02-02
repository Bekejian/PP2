word = str(input())
def palin(word):
    for i in range (0,len(word)//2):            #//2 可以节省时间
        if word[i]!=word[len(word)-i-1] :       
            return False
    return True
print(palin(word))
