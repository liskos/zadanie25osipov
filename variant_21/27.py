import sys

sys.stdin = open(file='Задание 27/Файл - А.txt')
n = int(input())
min_23_ch, min_ch, min_23_ne, min_ne = 9999999, 9999999, 9999999, 9999999
for _ in range(n):
    a = int(input())
    if a % 23 == 0 and a % 2 == 0:
        min_23_ch = min(min_23_ch, a)
    elif a % 23 == 0 and a % 2 == 1:
        min_23_ne = min(min_23_ne, a)
    elif a % 2 == 0:
        min_ch = min(min_ch, a)
    elif a % 2 != 0:
        min_ne = min(min_ne, a)
print(min_23_ne, min(min_ch, min_23_ch), min_23_ne + min(min_ch, min_23_ch))
print(min_23_ch, min(min_ne, min_23_ne), min_23_ch + min(min_ne, min_23_ne))
