import sys
sys.stdin = open(file='data/32/27-32b.txt')
n = int(input())
s = 0
r = [10001] * 11
for _ in range(n):
    a, b, c = sorted(map(int, input().split()))
    s += a
    for i in range(11):
        r[(b - a + i) % 11] = min(r[(b - a + i) % 11], b - a + r[i])
        r[(c - a + i) % 11] = min(r[(c - a + i) % 11], c - a + r[i])
    r[(b - a) % 11] = min(r[(b - a) % 11], b - a)
    r[(c - a) % 11] = min(r[(c - a) % 11], c - a)
if s % 11 != 0:
    s = s + r[-s % 11]
print(s)
