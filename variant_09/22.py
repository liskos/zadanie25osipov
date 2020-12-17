def f(x):
    a = 1
    while x > 0:
        a *= x % 7
        x = x // 7
    return a


for i in range(10000):
    if f(i) == 48:
        break
print(i)
