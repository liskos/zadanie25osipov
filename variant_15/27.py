import sys
sys.stdin = open(file='Задание 27/27-B.txt', mode='r', encoding='utf8')
n = int(input())
a = []
k = 0
for i in range(n):
    a.append(int(input()))
for i1 in range(1, n):
    for i2 in range(i1):
        if a[i1] > a[i2] and (a[i1]+a[i2]) > 50:
            k+=1
print(k)
