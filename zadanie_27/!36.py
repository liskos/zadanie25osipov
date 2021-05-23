import sys


def NOD(a, b):
    d = 1
    for i in range(2, a+1):
        if a % i == 0 and b % i == 0:
            d = i
    return d


sys.stdin = open(file='data/36/27-36b.txt')
n = int(input())
s = 0
r = [10000] * 10
for _ in range(n):
    a, b, c = sorted(map(int, input().split()))
    d = [NOD(c, b), NOD(c, a), NOD(b, a)]
    d.sort()
    s += d[2]
    r1, r2 = d[2] - d[1], d[2] - d[0]
    for i in range(10):
        r[(r1 + i) % 10] = min(r[(r1 + i) % 10], r1 + r[i])
        r[(r2 + i) % 10] = min(r[(r2 + i) % 10], r2 + r[i])
    r[r1 % 10] = min(r[r1 % 10], r1)
    r[r2 % 10] = min(r[r2 % 10], r2)
if s % 10 != 0:
    s -= r[s % 10]
print(s)
