import sys
sys.stdin = open(file='Задание 26/26.txt')
s, n = map(int, input().split())
a = []
v, k = 0, 0
l = 9999999
for _ in range(n):
    a.append(int(input()))
a.sort()
for i in range(n):
    if v + a[i] <= s:
        v += a[i]
        k += 1
    else:
        l = min(i, l)
print(k, v - a[l], s)
print(a[l:])
