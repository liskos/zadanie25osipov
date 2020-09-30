w = '1' * 63 + '2' * 61
while '111' in w:
    w = w.replace('111', '22', 1)
    w = w.replace('2222', '1', 1)
print(w)
