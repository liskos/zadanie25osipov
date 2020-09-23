def proverka(n):
    if n % 5 != 0:
        return False
    if len(set(str(n))) != 7:
        return False
    part1 = list(map(int, str(n)[::2]))
    part2 = list(map(int, str(n)[1::2]))
    if is_chet(part2) and is_notchet(part1):
        return True
    if is_chet(part1) and is_notchet(part2):
        return True


def is_chet(args):
    for x in args:
        if x % 2 != 0:
            return False
    return True


def is_notchet(args):
    for x in args:
        if x % 2 == 0:
            return False
    return True


a = []
for i in range(10**6, 10**7):
    if proverka(i):
        a.append(i)
print(a)
print(len(a))
