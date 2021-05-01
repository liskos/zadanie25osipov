import sys
sys.stdin = open(file='data/7/27-7b.txt')
n = int(input())
max7 = 0
maxnot7 = 0
for i in range(n):
    a = int(input())
    if a % 7 == 0 and a % 49 != 0:
        if max7 < a:
            max7 = a
    elif a % 7 != 0:
        if maxnot7 < a:
            maxnot7 = a
print(max(max7 * maxnot7, 1))
