import sys
sys.stdin = open(file='data/28/27-28b.txt')
n = int(input())
s = 0
minr = 99999
for i in range(n):
    a, b = map(int, input().split())
    s += min(a, b)
    r = abs(a - b)
    if minr > r and r % 8 != 0:
        minr = r
if s % 8 == 2:
    s += minr
print(s)
