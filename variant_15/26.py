import sys
sys.stdin = open(file='Задание 26/26.txt', mode='r', encoding='utf8')
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
print(a)
#???