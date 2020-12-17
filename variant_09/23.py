def f22(x):
    if x == 1:
        k = 1
    elif x > 0:
        k = f22(x - 1)
    else:
        k = 0
    if x % 3 == 0 and ((22 > (x // 3) > 1 and x <= 22) or (x // 3) >= 22):
        k += f22(x // 3)
    return k


print(f22(70))
