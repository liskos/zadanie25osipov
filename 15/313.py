def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((5*y+7*x)!=129) or (3*x >a)or (4*y>a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
