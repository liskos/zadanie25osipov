file = open(file='Задание 24/24.txt', mode='r', encoding='utf8')
k = 0
x = 0
for line in file:
    k = line.count('JBOSS') + line.count('BOSSJ') + line.count('JBOSSJ')
    x = line.count('BOSS')
print(x - k)
