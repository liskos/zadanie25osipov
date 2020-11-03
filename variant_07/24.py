file = open(file='Задание 24/24.txt', mode='r', encoding='utf8')
k = 0
n = 0
ls = ''
for i in file:
    if 'X' in i:
        if n > 0 and ls != 'X':
            n = 0
        elif n == 9:
            k += 1
            n = 0
        else:
            n += 1
    if 'Y' in i:
        if n > 0 and ls != 'Y':
            n = 0
        elif n == 6:
            k += 1
            n = 1
        else:
            n += 1
    if 'Z' in i:
        if n > 0 and ls != 'Z':
            n = 0
        elif n == 4:
            k += 1
            n = 0
        else:
            n += 1
    ls = i
print(k)
# знаю: в программе ошибка, но не смог сообразить: что не так.