import sys
sys.stdin = open(file='Задание 27/Файл - B.txt')
n = int(input())
min_23_1_ch = 9999999
min_oth_ch = 9999999
min_23_1_ne = 9999999
min_oth_ne = 9999999
for _ in range(n):
    a = int(input())
    if a % 2 == 0:
        if a % 23 == 0:
            min_oth_ch = min(min_oth_ch, min_23_1_ch)
            min_23_1_ch = min(min_23_1_ch, a)
        else:
            min_oth_ch = min(min_oth_ch, a)
    else:
        if a % 23 == 0:
            min_oth_ne = min(min_oth_ne, min_23_1_ne)
            min_23_1_ne = min(min_23_1_ne, a)
        else:
            min_oth_ne = min(min_oth_ne, a)
if min_23_1_ch == 9999999 or min_oth_ch == 9999999 or min_23_1_ne == 9999999 or min_oth_ne == 9999999:
    print(0, 0)
elif (max(min_23_1_ch, min_oth_ne) - min(min_23_1_ch, min_oth_ne)) > (max(min_23_1_ne, min_oth_ch) - min(min_23_1_ne, min_oth_ch)):
    print(min_23_1_ch, min_oth_ne)
else:
    print(min_23_1_ne, min_oth_ch)