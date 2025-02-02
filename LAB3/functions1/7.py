L=list(map(int,input().split()))
def array_check(L):
    for i in range (0,len(L)-1):
        if L[i]==3 and L[i+1]==3 :
            return True
    return False
print(array_check(L))

  