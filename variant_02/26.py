import sys

file = open(file="Задание 26/26.txt", mode="r", encoding="utf8")
sys.stdin = file

s, n = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
b = a.copy()
a.sort(reverse=True)
summa = 0
max_i = 0
new_a = []
for i in range(n):
    if summa + a[i] > s:
        continue
    summa = summa + a[i]
    new_a.append(a[i])
element_count = b.count(new_a[-1])

print(len(new_a), b.index(new_a[-1]))
