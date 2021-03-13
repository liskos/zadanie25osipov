def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((y+7*x)!=498) or ((x +18)>a)or ((6*y-3)>a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
