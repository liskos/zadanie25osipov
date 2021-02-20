def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((x <=8) or ((x * x + 3 * x) >= a)) and (((y * y + 5 * y) <= a) or (y >= 4))):
                return False
    return True


a = 0
for x in range(1, 1000):
    if f(x):
        a += 1
print(a)
