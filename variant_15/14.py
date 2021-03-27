s = 43 * 7 ** 103 - 21 * 7 ** 57 + 98
s7 = 0
while s > 0:
    s7 += s%7
    s = s//7
print(s7)
