from itertools import permutations
s=str(input())
def print_perm(s):
    perms=permutations(s)
    for p in perms:
        print("".join(p))           
print_perm(s)


'''
p = ('a', 'b', 'c')
print("".join(p))   这两行会output : abc （也就是把它们连在一起）
'''  