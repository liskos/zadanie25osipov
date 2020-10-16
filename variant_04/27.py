import sys
file = open(file="Задание 27/27-A.txt", mode="r", encoding="utf8")
sys.stdin = file

n = int(input())
a = []
maximum = 0
max_proizved = 0
for i in range(8):
    a.append(int(input()))
for i in range(8, n):
    x = int(input())
    maximum = max(a[i % 8], maximum)
    max_proizved = max(x * maximum, max_proizved)
    a[i % 8] = x
print(max_proizved)