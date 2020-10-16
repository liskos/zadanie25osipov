def kalk(a, b):
    if a == b:
        return 1
    if b < a:
        return 0
    return kalk(a, b-1) + kalk(a, b-10)

print(kalk(10, 33))