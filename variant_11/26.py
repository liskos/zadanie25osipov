import sys
file = open(file='Задание 26/26.txt', mode='r')
sys.stdin = file
n, k, m = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
print(a[k-1], a[k+m-1])
