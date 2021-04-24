import sys
sys.stdin = open(file='data/24/27-24b.txt')
n = int(input())
s = 0
minr = 99999
for i in range(n):
    a, b = map(int, input().split())
    s += min(a, b)
    r = abs(a - b)
    if r < minr and r != 0:
        minr = r
if s % 10 == 6:
    s += minr
print(s)
