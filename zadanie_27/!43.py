import sys
sys.stdin = open(file='data/43/27-43b.txt')
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
    s1, s2, s3 = s1 + c, s2 + b, s3 + a
if s1 % 2 != s2 % 2:
    if s1 % 2 == 0:
        print(s3 + minra_b)
    else:
        print(s3 + minra_c)
elif s1 % 2 == s2 % 2 and s1 % 2 != 0 and minrb_c == 100000:
    print(s3 + minra_c + minra_b)
else:
    print(s3)