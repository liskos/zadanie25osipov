import sys
sys.stdin = open(file='data/4/27-4b.txt')
n = int(input())
s = 0
r = [10001 for _ in range(5)]
for _ in range(n):
    a, b = sorted(map(int, input().split()))
    s += b
    for i in range(5):
        r[(b - a + i) % 5] = min(r[(b - a + i) % 5], b - a + r[i])
    r[(b - a) % 5] = min(r[(b - a) % 5], b - a)
if s % 5 != 0:
    s = s - r[s % 5]
print(s)
