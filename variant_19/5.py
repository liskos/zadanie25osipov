def f(x):
    if x % 2 == 0:
        x = x * 4 + 1
    else:
        x = x * 4 + 2
    return x


for i in range(-10000, 10000):
    if f(i) > 138:
        print(i)
        break