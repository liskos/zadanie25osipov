import sys
sys.stdin = open(file='data/29/27-29b.txt')
n = int(input())
s = 0
minr = 99999
for i in range(n):
    a, b, c = sorted(map(int, input().split()))
    s += b + c
    if (c - a) % 5 != 0:
        minr = min(c - a, minr)
    if (b - a) % 5 != 0:
        minr = min(b - a, minr)
if s % 5 == 0:
    s -= minr
print(s)
