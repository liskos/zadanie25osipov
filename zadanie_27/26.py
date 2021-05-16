import sys
sys.stdin = open(file='data/26/27-26b.txt')
n = int(input())
s = 0
r = [10001] * 16
for _ in range(n):
    a, b = sorted(map(int, input().split()))
    s += a
    for i in range(16):
        r[(b - a + i) % 16] = min(r[(b - a + i) % 16], b - a + r[i])
    r[(b - a) % 16] = min(r[(b - a) % 16], b - a)
if s % 16 != 15:
    s = s + r[(15 - s) % 16]
print(s)
