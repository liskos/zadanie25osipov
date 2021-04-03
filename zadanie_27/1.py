import sys
sys.stdin = open(file='data/1/27-1a.txt')
n = int(input())
s = 0
minr = 99999
for i in range(n):
    a, b = map(int, input().split())
    s += min(a, b)
    r = abs(a - b)
    if r < minr and r % 3 != 0:
        minr = r
if s % 3 ==0:
    s += minr
print(s)
