a = []
for i in range(809041920, 3559981057, 4):
    if i % 13 == 0 and i % 7 != 0 and i % 9 != 0 and i % 11 != 0:
        a.append(i)
print(min(a), len(a))
