x = 125 + 25 ** 3 + 5 ** 9
s = ""
while x > 0:
    s = str(x % 5) + s
    x = x // 5
print(s.count("0"))