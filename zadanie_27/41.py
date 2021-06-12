import sys
sys.stdin = open(file='data/41/27-41a.txt')
n = int(input())
minr = 100000
s1, s2, s3 = 0, 0, 0
for i in range(n):
    a, b, c = sorted(map(int, input().split()))
    ra_b, ra_c = b - a, c - a
    if ra_b % 2 != 0:
        minr = min(minr, ra_b)
    if ra_c % 2 != 0:
        minr = min(minr, ra_c)
    s1, s2, s3 = s1 + c, s2 + b, s3 + a
if s1 % 2 == s2 % 2:
    print(s3 + minr)
else:
    print(s3)
