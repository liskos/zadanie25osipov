m = []
for a in range(1000):
    k = 0
    for x in range(1000):
        if not((x & a != 0) or (x & 41 == 0) or (x & 37 == 0)):
            k += 1
    if k == 1000:
        m.append(a)
print(max(m))
