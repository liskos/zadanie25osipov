m = []
for a in range(1000):
    k = 0
    for x in range(1000):
        if (x & 30 != 4) or (x & 35 != 1) or (x & a == 0):
            k += 1
    if k == 1000:
        m.append(a)
print(min(m), max(m))
