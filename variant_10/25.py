def f(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


a = 0
for i in range(1542, 9413):
    if f(i):
        a += 1
print(a)
