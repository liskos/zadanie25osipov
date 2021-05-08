import sys
sys.stdin = open(file='data/11/27-11a.txt')
n = int(input())
s = 0
r = [10001 for _ in range(8)]
for _ in range(n):
    a, b, c = sorted(map(int, input().split()))
    s += c
    for i in range(8):
        r[(c - b + i) % 8] = min(r[(c - b + i) % 8], c - b + r[i])
        r[(c - a + i) % 8] = min(r[(c - a + i) % 8], c - a + r[i])
    r[(c - b) % 8] = min(r[(c - b) % 8], c - b)
    r[(c - a) % 8] = min(r[(c - a) % 8], c - a)
if s % 8 != 0:
    s = s - r[s % 8]
print(s)
