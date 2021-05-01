import sys
sys.stdin = open(file='data/8/27-8b.txt')
n = int(input())
a = [int(input()), int(input()), int(input()), int(input()), int(input())]
mins = 99999999
for i in range(5, n):
    a.append(int(input()))
    s = a[i]**2 + min(a[:i-4])**2
    if s < mins:
        mins = s
print(mins)
