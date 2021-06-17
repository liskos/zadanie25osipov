def f(s):
    n = 80
    while s + n < 160:
        s += 15
        n -= 10
    return s


for i in range(-1000, 1000):
    if f(i) <= 100:
        print(i)
        break
