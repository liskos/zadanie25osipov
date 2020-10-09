def f(s):
    n = 0
    while s - n > 0:
        s -= 10
        n += 15
    return n


a = []
for i in range(1, 10000):
    if f(i) == 165:
        a.append(i)
print(max(a))
