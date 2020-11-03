def f(x):
    if x % 2 == 0:
        x = x * 4 + 1
    else:
        x = x * 4 + 2
    return x


i = 0
while f(i) < 96:
    i += 1
print(i)
