def f(a):
    for x in range(1, 100000):
        if not(x % a != 0 or x % 24 != 0 or x % 16 == 0):
            return False
    return True


for a in range(1, 10000):
    if f(a):
        print(a)
        break
