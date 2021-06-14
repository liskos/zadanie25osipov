import sys
sys.stdin = open(file='Задание 26/26.txt')
n, k, m = map(int, input().split())
a = sorted([int(input()) for _ in range(n)])
print(min(a[n-m:]), sum(a[:k])//k)
