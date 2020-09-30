def algor(a, b):
    if a == b:
        return 1
    if b < a:
        return 0
    if b % 2 == 0:
        return algor(a, b-2) + algor(a, b // 2) + algor(a, b - 3)
    return algor(a, b-2) + algor(a, b - 3)


print(algor(2, 10) * algor(10, 21))
