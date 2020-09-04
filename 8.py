# допускается также
# использовать две
# целочисленные переменные x и y
a = []
n = 30
for i in range(0, n):
    a.append(int(input()))
b = []
for i in range(0, n):
    if a[i] >= 180:
        b.append(a[i])
print(min(b))