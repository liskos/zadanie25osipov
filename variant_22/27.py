import sys
sys.stdin = open(file='Задание 27/Файл - B.txt')
n = int(input())
m_37ch, m_37nech, mch, mnech = 0, 0, 0, 0
for _ in range(n):
    a = int(input())
    if a % 2 == 0:
        if a % 37 == 0:
            m_37ch = max(m_37ch, a)
        else:
            mch = max(mch, a)
    else:
        if a % 37 == 0:
            m_37nech = max(m_37nech, a)
        else:
            mnech = max(mnech, a)
a1, a2 = m_37ch + max(mnech, m_37nech), m_37nech + max(m_37ch, mch)
if a1 > a2:
    print(m_37ch, max(mnech, m_37nech))
elif a1 < a2:
    print(m_37nech, max(m_37ch, mch))
elif max(mnech, m_37nech) > max(m_37ch, mch):
    print(m_37nech, max(m_37ch, mch))
else:
    print(m_37ch, max(mnech, m_37nech))
