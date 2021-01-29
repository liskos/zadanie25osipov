m = []
for a in range(75, 125):
    k = 0
    for x in range(1000):
        if (x & 56 == 0) and (x & 43 == 0) or (x & a != 0):
            k += 1
    if k == 1000:
        m.append(a)
print(min(m))
