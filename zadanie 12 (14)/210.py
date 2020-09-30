w = '1' * 95 + '7' * 31
while '1111' in w:
    w = w.replace('1111', '7', 1)
    w = w.replace('77', '1', 1)
print(w)
