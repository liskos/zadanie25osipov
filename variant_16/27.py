import sys
sys.stdin = open(file='Задание 27/Файл - B.txt')
n = int(input())
s = 0
minr = 99999
for i in range(n):
    a, b = map(int, input().split())
    s += max(a, b)
    r = abs(a-b)
    if r < minr and r%5 != 0:
        minr = r
if s % 5 ==0:
    s -= minr
print(s)
