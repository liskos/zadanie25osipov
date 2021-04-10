import sys
sys.stdin = open(file='data/3/27-3b.txt')
n = int(input())
s = 0
min_r1a = 9999
min_r1b = 9999
min_r2 = 9999
for i in range(n):
    a, b = map(int, input().split())
    s += min(a, b)
    r = abs(a - b)
    if r % 3 == 2 and min_r2 > r:
        min_r2 = r
    if r % 3 == 1:
        if min_r1a > r:
            min_r1b = min_r1a
            min_r1a = r
        elif min_r1b > r:
            min_r1b = r
if s % 3 == 1:
    s += min_r1a
if s % 3 == 2:
    if min_r2 > (min_r1a + min_r1b):
        s += min_r1a + min_r1b
    else:
        s += min_r2
print(s)
