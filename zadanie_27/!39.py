import sys
sys.stdin = open(file='data/39/27-39b.txt')
n = int(input())
a = [0] * 1000
for _ in range(n):
    b = int(input())
    a[b] += 1
otv = 0
for i in range(1000):
    not_i = str(i)
    not_i = not_i[-1::-1]
    for n in range(min(a[i]//2, a[int(not_i)]//2)):
        otv += i
    a[i] = (a[i] % 2) * i
print(otv * 2 + max(a))
