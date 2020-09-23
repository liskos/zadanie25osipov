a = []
for i in range(8800, 55536):
    s = str(i)
    p = 1
    for digit in s:
        p *= int(digit)
    if ('7' in s) and (p > 35):
        a.append(i)
print(max(a), len(a))
