def f(x):
    x = str(x)
    a1 = sum(map(int, x[:2]))
    a2 = sum(map(int, x[2:]))
    return str(min(a1, a2)) + str(max(a1, a2))


for x in range(1000, 10000):
    if f(x) == '1113':
        print(x)
        break

