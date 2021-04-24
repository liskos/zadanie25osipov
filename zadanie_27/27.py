import sys
sys.stdin = open(file='data/27/27-27b.txt')
n = int(input())
s = 0
minr = 99999
for i in range(n):
    a, b = map(int, input().split())
    s += max(a, b)
    r = abs(a - b)
    if r < minr and r != 0:
        minr = r
if s % 16 == 10:
    s -= minr
print(s)
