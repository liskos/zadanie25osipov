def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((y * y >= a) or (y <= 14)) and ((x > 13) or (x * x < a))):
                return False
    return True


for x in range(1, 1000):
    if f(x):
        print(x)
        break