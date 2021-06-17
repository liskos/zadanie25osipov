import sys
sys.stdin = open(file='26-.txt')
n, k, m = map(int, input().split())
a = sorted([int(input()) for _ in range(n)])
print(a[-m])
print(sum(a[:k])//k)
