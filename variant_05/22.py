def f(x):
    a, b = 0, 1
    while x > 0:
        a += 1
        if x % 14 != 0:
            b = b * (x % 14)
        x = x // 14
    return a, b


k =0
for i in range(1000):
    a, b = f(i)
    if a == 2 and b == 12:
        k +=1
print(k)
