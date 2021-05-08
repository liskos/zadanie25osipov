import sys
sys.stdin = open(file='data/14/27-14b.txt')
n = int(input())
a = [0,0,0,0, 0,0,0,0, 0,0,0,0]
k = 0
for i in range(n):
    ch = int(input())
    k += a[- ch % 12]
    a[ch % 12] += 1
print(k)
