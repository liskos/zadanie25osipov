def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((x >11) and ((x * x + 3 * x) <= a) or ((y * y + 5 * y) > a) and (y < 6)):
                return False
    return True


a = 0
for x in range(1, 1000):
    if f(x):
        a += 1
print(a)
