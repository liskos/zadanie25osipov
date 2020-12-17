n = 81 ** 17 + 3 ** 24 - 45
k = ''
while n > 9:
    k = str(n % 9) + k
    n = n // 9
f = k.count('8')
print(f)
