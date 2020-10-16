import sys
file = open(file="Задание 26/26.txt", mode="r", encoding="utf8")
sys.stdin = file

a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
print(sum(a[:4]))
