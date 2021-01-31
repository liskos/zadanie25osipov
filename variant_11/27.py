import sys
sys.stdin = open(file='Задание 27/27-A.txt', mode='r')
n = int(input())
x = [0,0,0,0,0]
s = 0
for i in range(5):
    a = int(input())
    if a % 31 == 0:
        x[i % 5] = x[(i - 1) % 5]+1
for i in range(5, n):
    a = int(input())
    if a % 31 == 0:
        s += i - 5 #!!!
        x[i%5] += 1
    else:
        s += x[i%5]
        x[i % 5] = x[(i - 1) % 5]
print(s)
