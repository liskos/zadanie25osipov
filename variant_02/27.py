import sys

file = open(file="Задание 27/27-A.txt", mode="r", encoding="utf8")
sys.stdin = file

n = int(input())

count = [0] * 10
for x in range(n):
    count[x % 10] += 1

rez = count[1] * count[9] + count[7] * count[3] + count[5] * (count[5] - 1) // 2 + \
      count[6] * count[4] + count[2] * count[8] + count[0] * (count[0] - 1) // 2
print(rez)
