def f(a):
    for k in range(1, 100):
        for m in range(1, 100):
            if not(((5*k+9*m)>121) or ((k-13)<=a)and ((m+12)<a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break