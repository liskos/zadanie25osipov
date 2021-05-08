import sys
sys.stdin = open(file='data/30/27-30b.txt')
n = int(input())
s = 0
minr = 99999
for i in range(n):
    a, b, c = map(int, input().split())
    s += min(a, b, c)
    r = a + b + c - max(a, b, c) - 2 * min(a, b, c)
    if r < minr and r % 7 != 0:
        minr = r
if s % 7 == 0:
    s -= minr
print(s)
