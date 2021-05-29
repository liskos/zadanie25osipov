import sys
sys.stdin = open(file='data/53/27-53b.txt')
n = int(input())
m1 = [1000100] * 3
m2 = [1000100] * 3
m3 = [1000100] * 3
for _ in range(n):
    a = int(input())
    for i in range(3):
        m3[(a + i) % 3] = min(m3[(a + i) % 3], m2[i % 2] + a)
    for i in range(3):
        m2[(a + i) % 3] = min(m2[(a + i) % 3], m1[i % 2] + a)
    m1[a % 3] = min(m1[a % 3], a)
print(m3[0])
