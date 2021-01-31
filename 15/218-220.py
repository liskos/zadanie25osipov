m = []
for r in range(100):
    k = 0
    for a in range(100):
        for x in range(1000):
            if (x & 54 != 0) and (x & 45 != 0) or (x & a == 0) or (x & r == 0):
                k += 1
    if k == 1000000:
        m.append(r)
print(min(m))
