w = '1' * 2019 + '3' * 2119
while '11' in w:
    w = w.replace('11', '2', 1)
    w = w.replace('22', '3', 1)
    w = w.replace('33', '1', 1)
print(w)
