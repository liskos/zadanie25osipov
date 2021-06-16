import sys
sys.stdin = open(file='26data/26-k5.txt')
n, k, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort(reverse=True)
print(a[m - 1])
print(sum(a[-k:])//k)
