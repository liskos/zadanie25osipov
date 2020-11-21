import sys
file = open(file='Задание 26/26.txt', mode='r', encoding='utf8')
sys.stdin = file
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
k = int(n // 5)
S = sum(a)
plata_b = int(0.8 * sum(a[:k]))
prosent_neb = (S * 0.6 - 0.8*sum(a[:k]))/sum(a[k:])
plata_neb = prosent_neb * a[-1]
print(plata_b, int(plata_neb))
