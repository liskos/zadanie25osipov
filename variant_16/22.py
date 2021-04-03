def f(x):
    a = 0
    b = 0
    while x > 0:
        a += 1
        b += x % 8
        x = x // 8
    if a == 2 and b == 5:
        return True
    return False


for i in range(1000, 0, -1):
    if f(i):
        print(i)
        break
###!!!!!