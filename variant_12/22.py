def f(x):
    a, b = 0, 1
    while x > 0:
        a = a + 1
        b = b * (x % 9)
        x = x // 9
    return a, b


k = 0
a, b = f(k)
while a != 3 and b != 18:
    k += 1
    a, b = f(k)
print(k)
