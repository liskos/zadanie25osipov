def f(x):
    a, b, c = x // 100, x // 10 % 10, x % 10
    r1, r2 = a + b, b + c
    return int(str(max(r1,r2)) + str(min(r1, r2)))


for i in range(999, 99, -1):
    if f(i) == 86:
        print(i)
        break
