k = 0
m = 0
for i in range(1016, 7938):
    if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
        k += 1
        m = i
print(k, m)