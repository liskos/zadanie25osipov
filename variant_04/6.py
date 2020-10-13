def algor(d):
    s, n = 0, 0
    while s < 111:
        s = s + 8
        n = n + d
    return n


for i in range(1, 10000):
    if algor(i) == 28:
        print(i, algor(i))


