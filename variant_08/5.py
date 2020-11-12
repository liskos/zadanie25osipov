def f(x):
    x = 255 - x
    return x


i = 0
while f(i) != 151:
    i += 1
print(i)
