def f(a):
    for x in range(100000):
        if not(x&51 == 0 or (x&42 != 0 or x&a != 0)):
            return False
    return True


for i in range(10000):
    if f(i):
        print(i)
        break
