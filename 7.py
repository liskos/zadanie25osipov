s = 0
k = 0
n = 30
for i in range(0, n):
    x = int(input())
    if x > 20:
        s += x
        k += 1
print(s/k)