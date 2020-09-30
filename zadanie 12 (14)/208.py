w = '1' * 46 + '2' * 31
while '1111' in w:
    w = w.replace('1111', '2', 1)
    w = w.replace('222', '1', 1)
print(w)
