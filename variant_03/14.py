a = 8 ** 2014 - 2 ** 614 + 45
s = ''
while a > 0:
    s = str(a % 2) + s
    a = a // 2
print(s.count('1'))
