import sys
sys.stdin = open(file='data/34/27-34b.txt')
n = int(input())
s = 0
r = [[],[],[], [],[],[]]
for i in range(n):
    a, b, c = map(int, input().split())
    s += a + b + c - max(a, b, c)
    r1 = max(a, b, c) - min(a, b, c)
    r2 = 2 * max(a, b, c) - a - b - c + min(a, b, c)
    r[r1%6].append(r1)
    r[r2 % 6].append(r2)
print(s, s%6)
for i in range(1, 6):
    r[i].sort()
    print(i, ')', r[i])
