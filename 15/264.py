def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((x>=a) or (x * x<=169)) and ((y*y>=16) or (y<=a))):
                return False
    return True


a = 0
for x in range(1, 1000):
    if f(x):
        a += 1
print(a)
