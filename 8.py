# допускается также
# использовать две
# целочисленные переменные x и y
a = []
n = 30
for i in range(0, n):
    a.append(int(input()))
b = []
for element in a:
    if element >= 180:
        b.append(element)
print(min(b))