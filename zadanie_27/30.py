import sys
sys.stdin = open(file='data/30/27-30b.txt')
n = int(input())
s = 0
minr = 10001
for i in range(n):
    a, b, c = sorted(map(int, input().split()))
    s += a
    if (b - a) % 7 != 0:
        minr = min(minr, b - a)
    if (c - a) % 7 != 0:
        minr = min(minr, c - a)
if s % 7 == 0:
    s += minr
print(s)
