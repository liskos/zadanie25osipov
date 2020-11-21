import sys
sys.stdin = open(file="Задание 27/27-B.txt")

chet = []
not_chet = []
count_chet = 0
count_not_chet = 0
n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        chet.append(count_chet)
        not_chet.append(count_not_chet)
        count_chet = 0
        count_not_chet = 0
    elif x % 2 == 1:
        count_not_chet += 1
    else:
        count_chet += 1
not_chet.append(count_not_chet)
chet.append(count_chet)
s = 0
for i in range(len(chet)-1):
    s += chet[i] * sum(chet[i+1:])
for i in range(len(not_chet)-1):
    s += not_chet[i] * sum(not_chet[i+1:])
print(s)
