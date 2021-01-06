def f(x):
    a, b = 0, 1
    while x > 0:
        a = a + 1
        b = b * (x % 7)
        x = x // 7
    if a == 3 and b == 24:
        return True
    else:
        return False


a = []
for i in range(1000):
    if f(i):
        a.append(i)
print(max(a))
