import sys


def NOD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a



sys.stdin = open(file='data/36/27-36b.txt')
n = int(input())
s = 0
r = [10000] * 10
for _ in range(n):
    a, b, c = map(int, input().split())
    d = sorted([NOD(c, b), NOD(c, a), NOD(b, a)])
    s += d[2]
    r1, r2 = d[2] - d[1], d[2] - d[0]
    t = r.copy()
    for i in range(10):
        t[(r1 + i) % 10] = min(r[(r1 + i) % 10], r1 + r[i])
    r = t.copy()
    r[r1 % 10] = min(r[r1 % 10], r1)
    t = r.copy()
    for i in range(10):
        t[(r2 + i) % 10] = min(r[(r2 + i) % 10], r2 + r[i])
    r = t.copy()
    r[r2 % 10] = min(r[r2 % 10], r2)
if s % 10 != 0:
    s -= r[s % 10]
print(s)
