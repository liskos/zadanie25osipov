def f(a):
    for k in range(1, 1000):
        for m in range(1, 1000):
            if not(((k+m)>12) or ((k-10)>a) and ((m+10)>a)):
                return False
    return True


for i in range(1000, -1000, -1):
    if f(i):
        print(i)
        break