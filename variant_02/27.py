import sys

file = open(file="Задание 27/27-A.txt", mode="r", encoding="utf8")
sys.stdin = file

n = int(input())
count_even_ost_1 = 0
count_even_ost_2 = 0
count_even_ost_3 = 0
count_even_ost_4 = 0
count_even_ost_0 = 0
count_odd_ost_1 = 0
count_odd_ost_2 = 0
count_odd_ost_3 = 0
count_odd_ost_4 = 0
count_odd_ost_0 = 0

for x in range(n):
    if x % 10 == 0:
        count_even_ost_0 += 1
    elif x % 10 == 1:
        count_odd_ost_1 += 1
    elif x % 10 == 2:
        count_even_ost_2 += 1
    elif x % 10 == 3:
        count_odd_ost_3 += 1
    elif x % 10 == 4:
        count_even_ost_4 += 1
    elif x % 10 == 5:
        count_odd_ost_0 += 1
    elif x % 10 == 6:
        count_even_ost_1 += 1
    elif x % 10 == 7:
        count_odd_ost_2 += 1
    elif x % 10 == 8:
        count_even_ost_3 += 1
    elif x % 10 == 9:
        count_odd_ost_4 += 1
rez = count_odd_ost_1 * count_odd_ost_4 + count_odd_ost_2 * count_odd_ost_3 + count_odd_ost_0 * (
            count_odd_ost_0 - 1) // 2
rez += count_even_ost_1 * count_even_ost_4 + count_even_ost_2 * count_even_ost_3 + count_even_ost_0 * (
        count_even_ost_0 - 1) // 2
print(rez)
