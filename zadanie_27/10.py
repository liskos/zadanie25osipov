import sys
sys.stdin = open(file='data/10/27-10a.txt')
n = int(input())
s = 0
r = 10001
for _ in range(n):
    a, b, c = sorted(map(int, input().split()))
    s += c
    if (c - b) % 4 != 0:
        r = min(r, c - b)
    if (c - a) % 4 != 0:
        r = min(r, c - a)
if s % 4 == 0:
    s -= r
print(s)
