N=int(input())
def numbers(N):
    for num in range(N+1):
        if num%2==0:
            yield str(num)
print(",".join(numbers(N)))
    


