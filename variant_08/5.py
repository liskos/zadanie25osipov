def f(x):
    s = ""
    for i in str(x):
        s += (4 - len(bin(int(i))[2:])) * "0" + bin(int(i))[2:]
    s1 = ""
    for i in s:
        if i == "0":
            s1 += "1"
        else:
            s1 += "0"
    return int(s1, 2)


i = 0
while f(i) != 151:
    i += 1
print(i)
