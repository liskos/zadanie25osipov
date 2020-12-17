def f(s):
    n = 4
    while s < 37:
        s += 3
        n *= 2
    return n


for i in range(100):
    if f(i) == 128:
        break
print(i)
