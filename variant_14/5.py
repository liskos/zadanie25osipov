def f(x):
    if x%2 == 0:
        x = 4*x
    else:
        x = 4*x + 3
    return x


for i in range(50,1,-1):
    if f(i)< 140:
        print(i)
        break