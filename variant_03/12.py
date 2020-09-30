s = 95 * "3"
while "333" in s or "999" in s:
    if "999" in s:
        s = s.replace("999", "3", 1)
    else:
        s = s.replace("333", "9", 1)
print(s)
