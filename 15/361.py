def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((a<x)or(a<y))or(a<=101-x-y)):
                return False
    return True


for i in range(10000, -10000, -1):
    if f(i):
        print(i)
        break