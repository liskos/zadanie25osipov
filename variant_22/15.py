def f(a):
    for x in range(1, 100000):
        if not(x % a != 0 or x % 15 == 0 and x % 6 == 0):
            return False
    return True


for i in range(1, 10000):
    if f(i):
        print(i)
        break
