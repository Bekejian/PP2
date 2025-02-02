L=list(map(int, input().split()))
def isprime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):       #这里的+1不是指传统意义上的加， 而是指包含sqrt(n),也就是 [a,b]
        if n % i == 0:
            return False
    return True 
def print_prime(L):
    for x in L:
        if isprime(x):
            print(x,end=" ")                 #这个可以把所有output写在一行中
print_prime(L)

    