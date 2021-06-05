import sys
sys.stdin = open(file='26data/26-1.txt')
s, n = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()
v, k = 0, 0
for i in range(n):
    if v + a[i] <= s:
        k += 1
        v += a[i]
print('максимальное число пользователей = ', k)
sv = s - v + a[k - 1]
m = max([a[i] for i in range(k-1, n) if sv >= a[i]])
print('максимальный размер имеющегося файла', m)