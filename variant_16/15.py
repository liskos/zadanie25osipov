def f(a):
    for x in range(10000000):
        if not(((x&a)==0) or ((x&12)!=0) or ((x&5)!=0)):
            return False
    return True


for i in range(10000, 0, -1):
    if f(i):
        print(i)
        break
