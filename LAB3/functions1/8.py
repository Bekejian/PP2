L=list(map(int,input().split()))
def list_check(L):
    sublist=[0,0,7]
    i=0
    for number in L :
        if number == sublist[i]:
            i=i+1
        if i == len(sublist):
            return True
    return False
print(list_check(L))

# 1 2 3 0 2 0 2 7
         


