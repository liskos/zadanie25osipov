def f(x):
    x = x * 6 + (x % 6) # в условии 7-ая, но в примере: 6-ая.
    x = x * 2 + (x % 2)
    return x


i = 0
while f(i) < 344:
    print(f(i), i)
    i += 1
