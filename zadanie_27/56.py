import sys
sys.stdin = open(file='data/56/27-56b.txt')
m1 = [0] * 6
m2 = [0] * 6
m3 = [0] * 6
m4 = [0] * 6
for _ in range(int(input())):
    a = int(input())
    for i in range(6):
        m4[(a + i) % 6] = max(m4[(a + i) % 6], m3[i] + a)
    for i in range(6):
        m3[(a + i) % 6] = max(m3[(a + i) % 6], m2[i] + a)
    for i in range(6):
        m2[(a + i) % 6] = max(m2[(a + i) % 6], m1[i] + a)
    m1[a % 6] = max(m1[a % 6], a)
print(m4[0])
