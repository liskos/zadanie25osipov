def devyt(x):
    s = ""
    while x > 0:
        s = str(x % 9) + s
        x = x // 9
    return s


a = []
for x in range(1, 10000):
    if len(devyt(x)) == 3 and devyt(x).count("3") > 0:
        y = x * 3
        if len(devyt(y)) == 3:
            a.append(x)
x = max(a) + min(a)
print(devyt(x))

