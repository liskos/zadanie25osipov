def f(a):
    for x in range(1000):
        for y in range(1000):
            if not((99 != y + 2 * x) or (a < x) or (a < y)):
                return False
    return True


a = 0
for i in range(1000):
    if f(i):
        a = i
print(a)
