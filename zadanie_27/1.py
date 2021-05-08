import sys
sys.stdin = open(file='data/1/27-1a.txt')
n = int(input())
s = 0
r = 10001
for i in range(n):
    a, b = sorted(map(int, input().split()))
    s += a
    if (b - a) % 3 != 0:
        r = min(r, b - a)
if s % 3 == 0:
    s += r
print(s)
