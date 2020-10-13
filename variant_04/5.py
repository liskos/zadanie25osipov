def algor(x):
    s = ""
    for i in range(8):
        s = str(x % 2) + s
        x = x // 2
    s1 = ""
    for i in range(8):
        if s[i] == "0":
            s1 += "1"
        else:
            s1 += "0"
    return int(s1, 2) + 1


for n in range(1, 128):
    if algor(n) == 221:
        print(n)