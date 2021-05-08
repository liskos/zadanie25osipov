import sys
sys.stdin = open(file='data/19/27-19b.txt')
n = int(input())
m_x = max_x = min_x = int(input())
for i in range(1, n):
    ch = int(input())
    time_max = max(max_x * ch, min_x * ch, ch)
    min_x = min(ch, max_x * ch, min_x * ch)
    max_x = time_max
    m_x = max(max_x, m_x)
print(m_x)