import sys
sys.stdin = open(file='data/2/27-2b.txt')
n = int(input())
s = 0
r = [10001 for _ in range(3)]
for _ in range(n):
    a, b = sorted(map(int, input().split()))
    s += b
    for i in range(3):
        r[(b - a + i) % 3] = min(r[(b - a + i) % 3], b - a + r[i])
    r[(b - a) % 3] = min(r[(b - a) % 3], b - a)
if s % 3 != 0:
    s = s - r[s % 3]
print(s)
