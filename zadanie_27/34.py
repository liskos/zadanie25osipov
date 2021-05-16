import sys
sys.stdin = open(file='data/34/27-34b.txt')
n = int(input())
s = 0
r = [10001] * 6
for _ in range(n):
    a, b, c = sorted(map(int, input().split()))
    s += a + b
    for i in range(6):
        r[(c - b + i) % 6] = min(r[(c - b + i) % 6], c - b + r[i])
        r[(c - a + i) % 6] = min(r[(c - a + i) % 6], c - a + r[i])
    r[(c - b) % 6] = min(r[(c - b) % 6], c - b)
    r[(c - a) % 6] = min(r[(c - a) % 6], c - a)
if s % 6 != 0:
    s = s + r[-s%6]
print(s)
