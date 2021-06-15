import sys
sys.stdin = open(file='26data/26-k4.txt')
n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort(reverse=True)
print(sum(a[k:2*k])//k)
print(sum(a[:k])//k)
