import sys
sys.stdin = open(file='26data/26-k3.txt')
n, k, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort(reverse=True)
print('минимальный балл призёра', a[m + k - 1])
print('минимальный балл победителя', a[k - 1])
