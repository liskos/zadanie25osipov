a = []
for i in range(100000, 1000000):
    if ((i // 100000) + (i // 10000 % 10) + (i // 1000 % 10)) == ((i // 100 % 10) + (i // 10 % 10) + (i % 10)):
        a.append(i)
print(sum(a))