import sys
sys.stdin = open(file='27-33b.txt')
n = int(input())
s = 0
r = [[], [], [], []]
for i in range(n):
    a = sorted(list(map(int, input().split())))
    s += a[2] + a[1]
    r[(a[2] - a[0]) % 4].append(a[2] - a[0])
    r[(a[1] - a[0]) % 4].append(a[1] - a[0])
print(s, s % 4)
for x in r:
    x.sort()
for i in range(4):
    x = [c for c in r[i] if c <= 39]
    print(i, x)