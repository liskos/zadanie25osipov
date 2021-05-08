import sys
sys.stdin = open(file='data/31/27-31b.txt')
n = int(input())
s = 0
minr = 99999
for i in range(n):
    a, b, c = map(int, input().split())
    s += a + b + c - max(a, b, c)
    r = a + b + c - max(a, b, c) - 2 * min(a, b, c)
    if r < minr and r % 9 != 0:
        minr = r
if s % 9 == 0:
    s -= minr
print(s)
