import sys
file = open(file='Задание 27/27-B.txt', mode='r', encoding='utf8')
sys.stdin = file
N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
b = []
for i1 in range(N):
    for i2 in range(i1, N):
        if i2 - i1 > 4:
            b.append(a[i1] * a[i2])
c = 0
for i in b:
    if i % 29 == 0:
        c += 1
print(c)
