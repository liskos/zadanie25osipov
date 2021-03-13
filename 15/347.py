def f(a):
    for t in range(1, 100):
        for m in range(1, 100):
            if not(((3*t+8*m)>89) or ((m)<a)and ((t)<=a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break