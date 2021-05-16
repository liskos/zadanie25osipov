import sys
sys.stdin = open(file='Задание 27/27_B.txt')
k = 109
n = int(input())
s = 0
minr = 99999
for i in range(n):
    a, b, c = sorted(map(int, input().split()))
    s += c
    if (c-b)%k != 0:
        minr = min(minr, c-b)
    if (c-a)%k != 0:
        minr = min(minr, c-a)
if s % k == 0:
    s -= minr
print(s)
