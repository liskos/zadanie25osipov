import sys
sys.stdin = open(file='26data/26-j2.txt')
n, k, t = int(input()), 0, 0
a = sorted([int(input()) for _ in range(n)])
sr = sum(a) / n
med = a[n // 2]
b = [i for i in a if sr <= i <= med or med <= i <= sr]
print(len(b))
print(sr)
print(med)
