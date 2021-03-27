s = 43 * 7 ** 103 - 21 * 7 ** 51 + 98
s7 = ''
while s > 0:
    s7 += str(s%7)
    s = s//7
for i in s7:
    s += int(i)
print(s)
