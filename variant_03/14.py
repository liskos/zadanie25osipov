x = 8 ** 2014 - 2 ** 614 + 45
s = ""
while x > 0:
    s = str(x % 2) + s
    x = x // 2
print(s.count("1"))
