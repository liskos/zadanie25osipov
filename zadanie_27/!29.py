import sys
sys.stdin = open(file='data/29/27-29b.txt')
n = int(input())
s = 0
minr = 99999
for i in range(n):
    a, b, c = map(int, input().split())
    s += a + b + c - min(a, b, c)
    r = a + b + c - max(a, b, c) - 2 * min(a, b, c)
    if minr > r:
        minr = r
if s % 5 == 0:
    s -= minr
print(s)
