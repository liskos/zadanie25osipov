k = 0
m = 48990
for i in range(16015, 48990):
    if (i % 7 == 0 or i % 11 == 0) and i % 9 != 0 and i % 12 != 0 and i % 13 != 0:
        k += 1
        if m > i:
            m = i
print(k, m)
