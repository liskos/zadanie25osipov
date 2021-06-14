file = open(file='Задание 24/24.txt')
k = "X"
for s in file:
    while k in s:
        k += "X"
print(len(k) - 1)
