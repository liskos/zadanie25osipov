import sys
sys.stdin = open(file='26data/26-j4.txt')
n = int(input())
proc = n // 10
a = sorted([int(input()) for _ in range(n)])
print(sum(a[proc:-proc]), a[-proc])
