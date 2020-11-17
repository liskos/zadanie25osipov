import sys
file = open(file='Задание 26/26.txt', mode='r', encoding='utf8')
sys.stdin = file
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
k = int(0.2 * n)
S = sum(a)
plata_b = int(0.8 * sum(a[0:k]))
plata_neb = int(0.6 * S - plata_b)
x = (plata_neb / S)
print(plata_b, int(x * min(a)))
