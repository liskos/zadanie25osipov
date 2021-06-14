def f(s):
    for k in range(3, 9):
        s += k
    return s


for i in range(10000):
    if f(i) > 100:
        print(i)
        break
