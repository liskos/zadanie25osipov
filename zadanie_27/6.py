import sys
sys.stdin = open(file='data/6/27-6b.txt')
n = int(input())
max1=0
maxd6_2=0
maxd6=0
maxd3=0
maxd2=0
for i in range(n):
    a = int(input())
    if max1 < a and a %6!=0:
        max1 = a
    if maxd6 <= a and a%6==0:
        maxd6_2 = maxd6
        maxd6 = a
    elif a > maxd6_2 and a%6==0:
        maxd6_2 = a
    if a%6!=0 and a%3==0 and maxd3 < a:
        maxd3 = a
    if a%6!=0 and a%2==0 and maxd2 < a:
        maxd2 = a
x1=max1*maxd6
x2=maxd6*maxd6_2
x3=maxd2*maxd3
print(max(x1, x2, x3))
