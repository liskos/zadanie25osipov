def f(d):
    n = 10
    s = 122
    while s // d > 0:
        s = s - d
        n = n + 5
    return n


for i in range(1, 100):
    if f(i) == 60:
        break
print(i)
