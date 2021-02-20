def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((y*y >= a) or (y <= 8)) and ((x > 5) or (x*x <= a))):
                return False
    return True


a = 0
for x in range(1, 1000):
    if f(x):
        a += 1
print(a)
