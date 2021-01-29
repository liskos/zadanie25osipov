m = []
for a in range(10, 51):
    k = 0
    for x in range(1000):
        if not(not((x & 56 == 0) or (x & 18 == 0) or (x & a != 0)) or ((x & 18 == 0) and (x & a == 0) and (x & 43 != 0))):
            k += 1
    if k == 1000:
        m.append(a)
print(max(m))
