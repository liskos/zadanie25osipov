def f(x):
    if x == 43:
        return 0
    if x < 7:
        return 0
    if x == 7:
        return 1
    if x % 2 == 0:
        return f(x - 2)
    return f(x - 2) + f((x-1) // 2) + f((x+1) // 2)


print(f(63))
