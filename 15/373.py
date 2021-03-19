def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((x-30)<a)and((15-y)<a)or(x*(y+3)>60)):
                return False
    return True


for i in range(10000):
    if f(i):
        print(i)
        break
