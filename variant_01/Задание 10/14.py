s = 125 + 25 ** 3 + 5 ** 9
print(s)
z = ""
while s > 0:
    z = str(s % 5) + z
    s = s // 5
print(z)
print(z.count('0'))
