import sys
sys.stdin = open(file='data/33/27-33b.txt')
n = int(input())
s = 0
r = [10001] * 4
for i in range(n):
    a, b, c = sorted(map(int, input().split()))
    s += c + b
    for i in range(4):
        r[(c - a + i) % 4] = min(r[(c - a + i) % 4], c - a + r[i])
        r[(b - a + i) % 4] = min(r[(b - a + i) % 4], b - a + r[i])
    r[(c - a) % 4] = min(r[(c - a) % 4], c - a)
    r[(b - a) % 4] = min(r[(b - a) % 4], b - a)
if s % 4 != 0:
    s = s - r[s % 4]
print(s)
