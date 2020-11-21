import sys

file = open(file="Задание 26/26.txt")
sys.stdin = file

a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
s = sum(a) * 0.90  # лимит объема сохранения
new_s = sum(a)
a.sort(reverse=True)
max_v = 0
i_max = 0
for i in range(n):
    new_s -= a[i] * 0.2  # объем файла уменьшается на 20% объема
    if s >= new_s:
        max_v = n - (i + 1)  # i+1 - количество сжатых файлов, n-(i+1) - кол-во несжатых файлов
        i_max = i
        break
new_s += a[i_max] * 0.2
for i in range(n):
    if new_s - a[i] * 0.2 > s:
        i_max = i
        break
print(max_v, a[i_max+1])
