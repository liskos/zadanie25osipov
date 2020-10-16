import sys
file = open(file="Задание 27/27-B.txt", mode="r", encoding="utf8")
sys.stdin = file

n = int(input())
s = 0
raznost = 10001
for i in range(n):
    a, b = map(int, input().split())
    big, little = max(a, b), min(a, b)
    s += big
    if ((big - little) % 2 == 1) and (big - little < raznost):
        raznost = big - little

if s % 2 == 1:
    s = s - raznost
print(s)
