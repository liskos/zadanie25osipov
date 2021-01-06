import sys
file = open(file='Задание 26/26.txt', mode='r', encoding='utf8')
sys.stdin = file
N, K = input().split()
N = int(N)
K = int(K)
a = []
for i in range(N):
    a.append(int(input()))
a.sort()
print(sum(a[K:]))
