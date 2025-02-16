N = int(input())
def countdown(n):
    while n>=0:
        yield n 
        n=n-1
for num in countdown(N):
    print(num)