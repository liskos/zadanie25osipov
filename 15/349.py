def f(a):
    for k in range(0, 1000):
        for m in range(0, 1000):
            if not(((k+9*m)>121) or ((k-13)<=a)and ((m+12)<a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break