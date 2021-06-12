import sys
sys.stdin = open(file='data/40/27-40b.txt')
n = int(input())
minr = 100000
s1, s2, s3 = 0, 0, 0
for i in range(n):
    a, b, c = sorted(map(int, input().split()))
    ra_c, rb_c = c - a, c - b
    if ra_c % 2 != 0:
        minr = min(minr, ra_c)
    if rb_c % 2 != 0:
        minr = min(minr, rb_c)
    s1, s2, s3 = s1 + a, s2 + b, s3 + c
if s1 % 2 == s2 % 2:
    print(s3 - minr)
else:
    print(s3)
