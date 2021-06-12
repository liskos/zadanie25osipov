import sys
sys.stdin = open(file='26data/26-3.txt')
s, n = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort()
i = 0
kol = 0
for k in range(n):
    if i + a[k] <= s:
        i += a[k]
        kol += 1
    else:
        break
print(kol)
print(s - i + a[kol - 1])
print(a[kol - 1:])
