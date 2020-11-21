a = 5 * 7 ** 3 + 50 * 49 + 21 * 125
b = a
s1 = ""
s2 = ""
while a > 0:
    s1 = str(a % 7) + s1
    a = a // 7
while b > 0:
    s2 = str(b % 5) + s2
    b = b // 5
s1 = sum(map(int, s1))
s2 = sum(map(int, s2))
if s1 > s2:
    print(s1-s2 + 7)
else:
    print(s2-s1 + 5)