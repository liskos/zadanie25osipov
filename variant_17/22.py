def f(x):
    a = 0
    b = 0
    while x > 0:
        a += 1
        b += x % 10
        x = x // 10
    if a == 2 and b == 9:
        return True
    return False


for i in range(10000, -10000, -1):
    if f(i):
        print(i)
        break
