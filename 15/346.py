def f(a):
    for k in range(1, 100):
        for n in range(1, 100):
            if not(((7*k+2*n)>17) or ((k)<a)and ((n)<=a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break