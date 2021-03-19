def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((y<=x*x-4*x-5)or(y<=a-(x-2)**2))==(y<=abs(x*x-4*x-5))):
                return False
    return True


for i in range(10000):
    if f(i):
        print(i)
