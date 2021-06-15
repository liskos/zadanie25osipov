import sys
sys.stdin = open(file='26data/26-j3.txt')
s, n = map(int, input().split())
a = sorted([int(input()) for _ in range(n)])
m, summa, k = 0, 0, 0
for i in range(n-1, -1, -1):
    if summa + a[i] <= s:
        m = a[i]
        summa += a[i]
        k += 1
print(k, m)
