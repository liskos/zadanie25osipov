import sys
file = open(file="Задание 26/26.txt", mode="r", encoding="utf8")
sys.stdin = file

a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
a.sort()
kol5 = n // 20
new_a = a[kol5:-kol5]
print(sum(new_a))
print(max(new_a))
