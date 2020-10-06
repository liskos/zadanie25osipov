def F(x):
    a, b = 0, 0
    while x > 0:
        a = a + 1
        b = b + (x % 8)
        x = x // 8
    return a, b


for i in range(1, 10000):
    a, b = F(i)
    if a == 3 and b == 12:
        print(F(i), i)
