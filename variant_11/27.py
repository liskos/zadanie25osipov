import sys
sys.stdin = open(file='Задание 27/27-B.txt', mode='r')

n = int(input())
k = 6  # Требуемое расстояние между элементами
otv = 0  # Ответ
count = 0  # Количество чисел делящихся на 31, без последних k элементов
mas = [int(input()) for _ in range(k)]  # Массив хранения последних k значений
for i in range(k + 1, n + 1):
    a = int(input())
    if mas[0] % 31 == 0:
        count += 1
    if a % 31 == 0:
        otv += i - k
    else:
        otv += count
    mas.pop(0)
    mas.append(a)  # Удаляем первый элемент и вставляем значение переменной a на последнее место
print(otv)
