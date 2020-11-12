def f(x):
    s = 5
    while x > 0:
        if x % 8 > 4:
            s = s + (x % 8)
        else:
            s = s * (x % 8)
        x //= 8
    return s


i = 1
while f(i) != 100:
    i += 1
print(i)
