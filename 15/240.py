def f(a):
    for y in range(1, 1000):
        for x in range(1, 1000):
            if not(((x > 9) or (x * x <= a)) and ((y * y > a) or (x <= 10))):
                return False
    return True


a = 0
for x in range(1, 1000):
    if f(x):
        a = x
print(a)
#???