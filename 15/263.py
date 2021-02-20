def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((y*y>=30) or (y < a)) and ((x>a) or (x*x<150))):
                return False
    return True


a = 0
for x in range(1, 1000):
    if f(x):
        a += 1
print(a)
