def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((x >6) and ((x * x) <= a) or ((y * y) >= a) and (y < 5)):
                return False
    return True


a = 0
for x in range(1, 1000):
    if f(x):
        a += 1
print(a)
