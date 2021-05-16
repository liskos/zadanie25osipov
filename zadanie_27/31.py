import sys
sys.stdin = open(file='data/31/27-31b.txt')
n = int(input())
s = 0
minr = 99999
for i in range(n):
    a, b, c = sorted(map(int, input().split()))
    s += a + b
    if (c - b) % 9 != 0:
        minr = min(minr, c - b)
    if (c - a) % 9 != 0:
        minr = min(minr, c - a)
if s % 9 == 0:
    s += minr
print(s)
