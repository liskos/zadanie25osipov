import sys
sys.stdin = open(file='data/38/27-38b.txt')
n = int(input())
a = [0] * 10
for _ in range(n):
    b = int(input())
    a[b%10] += 1
a[5] -= 2
st = '5' + '9' * (a[9] // 2) + '8' * (a[8] // 2) + '7' * (a[7] // 2) + '6' * (a[6] // 2) + '5' * (a[5] // 2) + '4' * (a[4] // 2) + '3' * (a[3] // 2) + '2' * (a[2] // 2) + '1' * (a[1] // 2) + '0' * (a[0] // 2)
for i in range(10):
    a[i] = (a[i] % 2) * i
otv = 0
for i in st:
    otv += int(i)
print(otv * 2 + max(a))
