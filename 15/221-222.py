m = []
for a in range(1000):
    k = 0
    for x in range(1000):
        if (x & 25 != 1) or (x & 34 != 2) or (x & a == 0):
            k += 1
    if k == 1000:
        m.append(a)
print(min(m), max(m))
