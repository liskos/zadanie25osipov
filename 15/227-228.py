m = []
for a in range(1000):
    k = 0
    for x in range(1000):
        if (x & a == 0) or (x & 55 == 33) or (x & 112 != 16):
            k += 1
    if k == 1000:
        m.append(a)
print(min(m), max(m))
