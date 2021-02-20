def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((x >= 3) or (x * x <= a)) and ((y * y >= a) or (y < 6))):
                return False
    return True


a = 0
for x in range(1, 1000):
    if f(x):
        a += 1
print(a)
