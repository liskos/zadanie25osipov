m = []
for a in range(256, 2567):
    if a % 7 == 0 and a % 21 != 0 and a % 23 != 0 and a % 31 != 0:
        m.append(a)
print(*m)
print(sum(m), max(m))
