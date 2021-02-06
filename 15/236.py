def f(a):
    for x in range(1, 1000):
        if (x & a !=0) and (x & 58 == 0) and (x & 22 == 0):
            return False
    return True


a = 0
for x in range(1, 1000):
    if f(x):
        a = x
print(a)
