import sys
sys.stdin = open(file='26data/26-k2.txt')
n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()
a = a[k:-k]
print('наибольшее достоверное измерение', a[-1])
print('целую часть среднего значения всех достоверных измерений', int(sum(a)/len(a)))
