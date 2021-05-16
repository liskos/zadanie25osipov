import sys
sys.stdin = open(file='data/25/27-25a.txt')
n = int(input())
s = 0
r = [10001] * 8
for _ in range(n):
    a, b = sorted(map(int, input().split()))
    s += b
    for i in range(8):
        r[(b - a + i) % 8] = min(r[(b - a + i) % 8], r[(i) % 8] + b - a)
    r[(b - a) % 8] = min(r[(b - a) % 8], b - a)
if s % 8 != 3:
    s = s - r[(s - 3) % 8]
print(s)
