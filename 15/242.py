def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((x > 11) or (x * x <= a)) and ((y * y >= a) or (y <= 12))):
                return False
    return True


for x in range(1, 1000):
    if f(x):
        print(x)
        break
