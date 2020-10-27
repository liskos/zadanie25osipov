import sys
file = open(file='Задание 27/27-B.txt')
sys.stdin = file
a = int(input())
chyot = 0
ne_chyot = 0
for i in range(a):
    n = int(input())
    if n % 2 == 0:
        chyot += 1
    else:
        ne_chyot += 1
print((chyot // 2) + (ne_chyot // 2))
