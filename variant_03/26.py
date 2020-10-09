import sys
file = open(file='Задание 26/26.txt', mode='r', encoding='utf8')
sys.stdin = file

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
print(sum(a[:10]))
