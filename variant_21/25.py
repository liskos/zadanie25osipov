def f(x):
    k = 0
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            if x // i == i:
                k += 1
            else:
                k += 2
    return [k, x]


a = []
for i in range(79201, 80001):
    a.append(f(i))
print(max(a, key=lambda x: (x[0],x[1])))
