a = 5 * 7 ** 3 + 50 * 49 + 21 * 125
b = a
s1 = 0
s2 = 0
while a > 0:
    s1 += a % 7
    a = a // 7
while b > 0:
    s2 += b % 5
    b = b // 5
if s1 > s2:
    print(7)
else:
    print(5)
