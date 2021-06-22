import sys
sys.stdin = open(file='26data/26-j8.txt')
n = int(input())
a = sorted([int(input()) for _ in range(n)])
k1, k2 = int(0.7 * n) - 1, n // 2 - 1
s1, s2 = [], []
for i in range(n):
    if i < k1:
        s1.append(0.7 * a[i])
    else:
        s1.append(0.6 * a[i])
    if i < k2:
        s2.append(0.6 * a[i])
    else:
        s2.append(0.65 * a[i])
sum1, sum2 = sum(s1), sum(s2)
if sum1 > sum2:
    print(int(sum1 - sum2), int(max(s1)))
else:
    print(int(sum2 - sum1), int(max(s2)))
