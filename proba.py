def is_latinica(x):
    return ("a" <= x <= "z") or ("A" <= x <= "Z")


def sdvig(stroka_sim):
    s = ""
    for sumvol in stroka_sim:
        if is_latinica(chr(ord(sumvol) + 1)):
            s += chr(ord(sumvol) + 1)
        else:
            s += chr(ord(sumvol) + 1 - 26)
    return s


s = input() + " "
new_str = ""
stroka = ""
for sumvol in s:
    if is_latinica(sumvol):
        stroka += sumvol
    else:
        for _ in range(len(stroka)):
            stroka = sdvig(stroka)
        new_str += stroka
        new_str += sumvol
        stroka = ""
print(new_str[:-1])
