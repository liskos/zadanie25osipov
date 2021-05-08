def f(x):
    a = []
    for i in range(2, int(x**0.5) +1):
        if x % i == 0:
            a.append(i)
            a.append(x//i)
    a = set(a)
    return sum(a)


k = 0
for i in range(350300, 999999):
    s = f(i)
    if s % 13 == 0:
        print(i, s//13)
        k += 1
        if k == 6:
            break
