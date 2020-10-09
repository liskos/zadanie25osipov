a = []
for i in range(1024, 28922):
    c = sum(list(map(int, str(i))))
    if i % c == 0:
        a.append(i)
print(sum(a))
