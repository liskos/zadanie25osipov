def f(a):
    for x in range(200):
        for y in range(200):
            if (((2 * x + y) != 100) or (x < y) or (a < x)) == False:
                return False
    return True


a = []
for i in range(200):
    if f(i):
        a.append(i)
print(max(a))
