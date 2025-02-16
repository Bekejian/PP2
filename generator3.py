N=int(input())
def three_four(N):
    for num in range(N+1):
        if num%3==0 and num%4==0:
            yield num
for num in three_four(N):
    print(num)
