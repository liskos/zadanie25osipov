import sys
sys.stdin = open(file='Задание 26/26.txt', mode='r', encoding='utf8')
n = int(input())
a = []
s = 0
for i in range(n):
    l = int(input())
    a.append(l)
    s +=l
a.sort(reverse=True)
print(s - sum(a[4:]))