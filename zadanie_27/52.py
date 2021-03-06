# В файле записана последовательность натуральных чисел. Гарантируется, что все числа различны.
# Из этой последовательности нужно выбрать три числа, чтобы их сумма делилась на 3 и была наибольшей.
# Какую наибольшую сумму можно при этом получить?

import sys
sys.stdin = open(file='data/52/27-52a.txt')
n = int(input())
m1 = [0] * 3
m2 = [0] * 3
m3 = [0] * 3
for _ in range(n):
    x = int(input())
    for i in range(3):
        m3[(x + i) % 3] = max(m3[(x + i) % 3], m2[i] + x)
    for i in range(3):
        m2[(x + i) % 3] = max(m2[(x + i) % 3], m1[i] + x)
    m1[x % 3] = max(m1[x%3], x)
print(m3[0])
