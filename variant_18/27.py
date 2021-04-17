import sys
sys.stdin = open(file='Задание 27/27-B.txt')
n = int(input())
s = 0
minr=999999
for i in range(n):
    a, b = map(int, input().split())
    s += max(a, b)
    r = abs(a-b)
    if r < minr and r != 0:
        minr = r
if s % 10 == 5:
    s -= minr
print(s)
