x = 9 ** 8 + 3 ** 5 - 2
k = ''
while x > 0:
    k += str(x % 3)
    x = x // 3
print(k.count('2'))
