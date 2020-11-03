def f(x):
    a, b = 0, 1
    while x > 0:
        a = a + 1
        b = b * (x % 7)
        x = x // 7
    return a, b


for x in range(100000):
    a, b = f(x)
    if a == 4 and b == 30:
        break
print(x)
