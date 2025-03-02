def check(t):
    return all(t) 

tuple = (1, 2, 3, 4, 5)
print(check(tuple))

tuple2 = (1, 2, 0, 4)
print(check(tuple2))

tuple3 = (True, True, False)
print(check(tuple3))