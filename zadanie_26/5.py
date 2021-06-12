import sys
sys.stdin = open(file='26data/26-5.txt')
s, n = map(int, input().split())
a = sorted([int(input()) for _ in range(n)])
v, kol = 0, 0
for k in range(n):
    if v + a[k] <= s:
        v += a[k]
        kol += 1
print(kol)
v -= a[kol - 1]
print(max([a[i] for i in range(kol - 1, n) if v + a[i] <= s]))
