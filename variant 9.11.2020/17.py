def f8(x):
    k = 0
    while x > 0:
        k += 1
        x = x // 8
    return k


def f6(x):
    k = 0
    while x > 0:
        k += 1
        x = x // 6
    return k


k, m = 0, 0
for i in range(1000, 70001):
    if f8(i) == 5 and f6(i) == 6 and i % 256 == 250:
        k += 1
        m = i
print(k, m)
