# Набор данных состоит из нечётного количества пар натуральных чисел.
# Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма выбранных чисел была максимальной при условии,
# что чётность этой суммы совпадает с чётностью большинства выбранных чисел.
# Определите максимальную сумму, которую можно получить при таком условии.
# Гарантируется, что удовлетворяющий условиям выбор возможен.
# 117046 411037387
import sys
sys.stdin = open(file='data/48/27-48b.txt')
n = int(input())
s = 0
nech = 0
m_chet, m_nech = [10001, 10001], [10001, 10001]
for _ in range(n):
    a, b = sorted(map(int, input().split()))
    s += b
    nech += b % 2
    if (b - a) % 2 == 1 and b % 2 == 0:
        m_chet.append(b - a)
        m_chet.sort()
        m_chet.pop(-1)
    elif (b - a) % 2 == 1 and b % 2 == 1:
        m_nech.append(b - a)
        m_nech.sort()
        m_nech.pop(-1)
chet = n - nech
print('чётных', chet)
print('нечётных', nech)
print('исходная сумма', s)
print(m_chet, m_nech)
if s % 2 == 0 and nech == chet + 1:
    s -= min(m_chet[0], sum(m_nech[:2]))
    print(1)
elif s % 2 == 1 and nech == chet - 1:
    s -= min(m_nech[0], sum(m_chet[:2]))
    print(2)
elif s % 2 == 1 and chet > nech:
    s -= min(m_chet + m_nech)
    print(3)
elif s % 2 == 0 and chet < nech:
    s -= min(m_chet + m_nech)
    print(4)
print('s=', s)
