def iun15(a, b):
    if b == 6:
        return 0
    if b == a:
        return 1
    if b < a:
        return 0
    if b % 3 == 0:
        return iun15(a, b-2) + iun15(a, b // 3)
    return iun15(a, b - 2)


print(iun15(1, 25) * iun15(25, 63))
