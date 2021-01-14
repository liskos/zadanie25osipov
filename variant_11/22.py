def f(x):
    a, b = 0, 1
    while x > 0:
        a = a + 1
        b = b * (x % 9)
        x = x // 9
    return a, b


m = []
for i in range(1000):
    a, b = f(i)
    if a == 3 and b == 24:
        m.append(i)
print(max(m))
