def f(a):
    for x in range(1, 21):
        for y in range(1, 41):
            if not(((y+2*x)<a) or (x>20)or (y > 40)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break