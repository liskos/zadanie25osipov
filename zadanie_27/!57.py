import sys
sys.stdin = open(file='data/57/27-57b.txt')
m1 = [1000000000] * 9
m2 = [1000000000] * 9
m3 = [1000000000] * 9
m4 = [1000000000] * 9
for _ in range(int(input())):
    a = int(input())
    for i in range(9):
        m4[(a + i) % 9] = min(m3[(a + i) % 9], m3[i] + a)
    for i in range(6):
        m3[(a + i) % 9] = min(m2[(a + i) % 9], m2[i] + a)
    for i in range(6):
        m2[(a + i) % 9] = min(m1[(a + i) % 9], m1[i] + a)
    m1[a % 6] = min(m1[a % 9], a)
print(m4[0])
