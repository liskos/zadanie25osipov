def f(d):
    n, s = 10, 101
    while d < s + n:
        s = s - 2 * d
        n += d
    return n


d = 1
while f(d) != 100:
    d += 1
print(d)
