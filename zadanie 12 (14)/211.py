w = '1' * 13 + '2' * 13 + '3' * 13
while '11' in w:
    w = w.replace('11', '2', 1)
    w = w.replace('22', '3', 1)
    w = w.replace('33', '1', 1)
print(w)
