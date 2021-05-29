import sys
sys.stdin = open(file='data/54/27-54b.txt')
n = int(input())
m1 = [0] * 4
m2 = [0] * 4
m3 = [0] * 4
m4 = [0] * 4
for _ in range(n):
    a = int(input())
    for i in range(4):
        m4[(a + i) % 4] = max(m4[(a + i) % 4], m3[i] + a)
    for i in range(4):
        m3[(a + i) % 4] = max(m3[(a + i) % 4], m2[i] + a)
    for i in range(4):
        m2[(a + i) % 4] = max(m2[(a + i) % 4], m1[i] + a)
    m1[a % 4] = max(m1[a % 4], a)
print(m4[0])
