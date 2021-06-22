import sys
sys.stdin = open(file='26data/26-j7.txt')
n = int(input())
a = sorted([int(input()) for _ in range(n)])
k_procmax = int(0.2 * n)
s1, s2 = 0.6 * sum(a), 0.8 * sum(a[:-k_procmax])
print(int(s2))
k_procmin = n - k_procmax + 1
procmin = (s1 - s2) / s1
print(int(procmin * a[0]))
