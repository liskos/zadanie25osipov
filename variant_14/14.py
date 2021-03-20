def f(x):
    s = ''
    while x > 0:
        s += str(x%4)
        x = x // 4
    return s


s = 16**18 * 4**10 - 4**6 - 16
print(f(s).count('3'))
