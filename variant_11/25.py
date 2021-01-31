def f(x):
    a = []
    if x % 2 == 1:
        for i in range(2, x):
            if x % i == 0:
                a.append(i)
    return a



for i in range(123, 1235):
    mas_del = f(i)
    if len(mas_del) == 4:
        print(i, mas_del)