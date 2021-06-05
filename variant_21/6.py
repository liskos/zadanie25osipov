def f(s):
    for k in range(4, 8):
        s *= k
    return s


for i in range(0, 100000):
    if f(i) >= 18500:
        print(i)
        break
