L=list(map(int,input().split()))
def uniquelist(L):
    uniqL=[]
    for num in L:
        if num not in uniqL:
            uniqL.append(num)
    return uniqL
print(uniquelist(L))
#print(" ".join(map(str, uniquelist(L))))
