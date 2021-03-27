a = []
for i in range(950, 4179):
    if i % 7 != 0 and i % 9 != 0 and i % 11 != 0:
        a.append(i)
print(a[0]*13*2**16, len(a))
