def f(n):
    n = bin(n)
    n = n[2:]
    k = 0
    for i in (n):
        k += int(i)
    r = n + str(k % 2)
    for i in (r):
        k += int(i)
    r = n + str(k % 2)
    r = int(r, 2)
    return r


for i in range(300):
    if f(i) > 170:
        break
print(i)
