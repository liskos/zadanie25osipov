m = []
for a in range(43, 56):
    k = 0
    for x in range(1000):
        if not(not((x & 17 == 0) or (x & a == 0) or (x & 58 != 0)) or ((x & 8 == 0) and (x & a != 0) and (x % 58 == 0))):
            k += 1
    if k == 1000:
        m.append(a)
print(min(m), max(m))
