import sys
file = open(file="Задание 27/27-B.txt", mode="r", encoding="utf8")
sys.stdin = file

n = int(input())
s = 0
min_raznost = 10001
for _ in range(n):
    a, b = map(int, input().split())
    little, big = min(a, b), max(a, b)
    s += little
    raznost = big - little
    if raznost % 6 != 0:
        min_raznost = min(min_raznost, raznost)
if s % 6 == 0:
    s += min_raznost
print(s)
