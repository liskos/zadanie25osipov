def algol(s):
    n = 0
    while s - n > 0:
        s = s - 10
        n = n + 15
    return n


x = 0
for i in range(0, 10000):
    if algol(i) == 165:
        x = i
print(x)
