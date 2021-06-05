import sys
sys.stdin = open(file='Задание 26/26.txt')
s, n = map(int, input().split())
v, k = 0, 0
a = [int(input()) for _ in range(n)]
a.sort()
for i in range(n):
    if v + a[i] <= s:
        v += a[i]
        k += 1
sv = s - v + a[k-1]
m =max([a[i] for i in range(k-1, n) if a[i] <= sv])
print("максимальное число пользователей", k)
print("максимальный размер который мог быть сохранен", m)
