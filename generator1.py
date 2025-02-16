N=int(input())
def sqr_gnerator(N):
    for number in range(1,N+1):
        yield number**2
for sqr in sqr_gnerator(N):
    print(sqr)

      