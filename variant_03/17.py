a = []
for i in range(1024, 616522):
    if i % 8 == 3 and i % 3 == 0:
        a.append(i)
print(sum(a), min(a))
