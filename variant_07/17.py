a = []
for i in range(4221, 17524):
    if i % 16 == 11 or i % 7 == 6:
        a.append(i)
print(sum(a), min(a))
