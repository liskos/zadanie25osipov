def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((x >a) and ((x * x) < 19) or ((y * y) > 91) and (y < a)):
                return False
    return True


a = 0
for x in range(1, 1000):
    if f(x):
        a += 1
print(a)
