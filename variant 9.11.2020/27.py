import sys
sys.stdin = open(file='27-B.txt')
n = int(input())
r = [1000000] * 4
s = 0
for _ in range(n):
    a, b, c = sorted(map(int, input().split()))
    s += c + b
    r1, r2 = c - a, b - a
    for i in range(4):
        r[(r1 + i) % 4] = min(r[(r1 + i) % 4], r[i] + r1)
    r[r1 % 4] = min(r[r1 % 4], r1)
    for i in range(4):
        r[(r2 + i) % 4] = min(r[(r2 + i) % 4], r[i] + r2)
    r[r2 % 4] = min(r[r2 % 4], r2)
if s % 4 != 0:
    s -= r[s % 4]
print(s)
