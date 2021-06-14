def f(x):
    k = 0
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if i == x // i:
                k += 1
            else:
                k += 2
    return k, x

a = []
for i in range(59999, 64001):
    a.append(f(i))
print(max(a))
