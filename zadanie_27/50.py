# Набор данных состоит из нечётного количества пар натуральных чисел.
# Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма выбранных чисел была максимальной при условии,
# что чётность этой суммы НЕ совпадает с чётностью большинства выбранных чисел. Определите максимальную сумму, которую
# можно получить при таком условии. Гарантируется, что удовлетворяющий условиям выбор возможен.
import sys
sys.stdin = open(file='data/50/27-50b.txt')
n = int(input())
s = 0
nech = 0
m_ch, m_ne = [10001, 10001], [10001, 10001]
for i in range(n):
    a, b = sorted(map(int, input().split()))
    s += b
    nech += b % 2
    if (b - a) % 2 == 1 and b % 2 == 0:
        m_ch.append(b - a)
        m_ch.sort()
        m_ch.pop(-1)
    elif (b - a) % 2 == 1 and b % 2 == 1:
        m_ne.append(b - a)
        m_ne.sort()
        m_ne.pop(-1)
chet = n - nech
print('chet = ', chet)
print('nechet = ', nech)
print(s)
if s % 2 == 1 and nech == chet + 1:
    s -= min(m_ch[0], sum(m_ne[:2]))
    print(1)
elif s % 2 == 0 and nech == chet - 1:
    s -= min(m_ne[0], sum(m_ch[:2]))
    print(2)
elif s % 2 == 1 and nech > chet:
    s -= min(m_ne + m_ch)
    print(3)
elif s % 2 == 0 and nech < chet:
    s -= min(m_ne + m_ch)
    print(4)
print(s)
