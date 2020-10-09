import sys
file = open(file='Задание 27/27-B.txt', mode='r', encoding='utf8')
sys.stdin = file

n = int(input())
s = 0
min_razn = 10000
for i in range(n):
    a, b = map(int, input().split())
    s += max(a, b)
    razn = max(a, b) - min(a, b)
    if razn % 2 == 1:
        min_razn = min(min_razn, razn)
if s % 2 == 0:
    s -= min_razn
print(s)