def f(x):
    k = 0
    m = 0
    for i in range(2, x):
        if x % i == 0:
            k += 1
            if m < i:
                m = i
    return k, m


for i in range(10331, 12357):
    c = i*i
    k, m = f(c)
    if k == 3:
        print(c, m)