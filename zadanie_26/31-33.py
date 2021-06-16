import sys
sys.stdin = open(file='26data/26-s1.txt')
n, m, s = int(input()), 0, 0
a = []
for _ in range(n):
    b = int(input())
    if b <= 200:
        s += b
    else:
        a.append(b)
a.sort()
s += sum(a[1::2])
print(s + 0.3 * sum(a[::2]))
print(max(a[::2]))
