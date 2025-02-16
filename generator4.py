a=int(input())
b=int(input())
def squares(a,b):
    for number in range(a,b+1):
        yield number**2
for square in squares(a,b):
    print(square)


