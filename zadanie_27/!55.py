import sys
sys.stdin = open(file='data/55/27-55b.txt')
n = int(input())
m1 = [1000000] * 4
m2 = [1000000] * 4
m3 = [1000000] * 4
m4 = [1000000] * 4
for _ in range(n):
    a = int(input())
    for i in range(4):
        m4[(a + i) % 4] = min(m4[(a + i) % 4], m3[i] + a)
    for i in range(4):
        m3[(a + i) % 4] = min(m3[(a + i) % 4], m2[i] + a)
    for i in range(4):
        m2[(a + i) % 4] = min(m2[(a + i) % 4], m1[i] + a)
    m1[a % 4] = min(m1[a % 4], a)
print(m4[0])
