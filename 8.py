# допускается также
# использовать две
# целочисленные переменные x и y
b = []
n = 30
for i in range(0, n):
    x = int(input())
    if x >= 180:
        b.append(x)
print(min(b))