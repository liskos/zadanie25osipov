import sys
sys.stdin = open(file='data/35/27-35b.txt')
n = int(input())
b = [0, 0]
k = 0
chet, nech = 0, 0
for _ in range(n):
    i = int(input())
    if i == 0:
        b[0] += chet
        b[1] += nech
        chet = 0
        nech = 0
    elif i % 2 == 0:
        chet += 1
        k += b[0]
    else:
        nech += 1
        k += b[1]
print(k)
