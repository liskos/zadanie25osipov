def f(a):
    for x in range(1, 10000):
        if not((x % 5940 == 0) or (x % a != 0) or (x % 6300)):
            return False
    return True


for a in range(1, 10000):
    if f(a):
        print(a)
        break
