m = []
for a in range(1000):
    k = 0
    for x in range(1000):
        if not(not ((x & a == 0) or (x & 62)) or ((x & 24) and (x & a != 0))):
            k += 1
    if k == 1000:
        m.append(a)
print(min(m))
