def f(a):
    for x in range(1, 10000):
        for y in range(1, 10000):
            if not((x >= 9) or ((5 * y) >= x) or ((2 * x * y) < a)):
                return False
    return True


for i in range(10000):
    if f(i):
        print(i)
        break