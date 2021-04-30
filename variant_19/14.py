s = 9 ** 7 + 3 ** 8 - 5
k = [0, 0, 0]
while s > 0:
    k[s%3] += 1
    s = s//3
print(k)