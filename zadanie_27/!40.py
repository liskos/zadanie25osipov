import sys
sys.stdin = open(file='data/40/27-40b.txt')
n = int(input())
minra_b, minra_c, minrb_c = 100000, 100000, 100000
s1, s2, s3 = 0, 0, 0
for i in range(n):
    a, b, c = sorted(map(int, input().split()))
    ra_b, ra_c, rb_c = b - a, c - a, c - b
    if ra_b % 2 != 0:
        minra_b = min(minra_b, ra_b)
    if ra_c % 2 != 0:
        minra_c = min(minra_c, ra_c)
    if rb_c % 2 != 0:
        minrb_c = min(minrb_c, rb_c)
    s1, s2, s3 = s1 + a, s2 + b, s3 + c
if s1 % 2 == s2 % 2 and minra_b == 100000:
    if minrb_c < minra_c:
        print(s3 - minrb_c)
    else:
        print(s3 - minra_c)
else:
    print(s3)
