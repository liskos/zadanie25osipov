w = '1' * 2019 + '2' * 2119
while '222' in w:
    w = w.replace('222', '1', 1)
    w = w.replace('111', '2', 1)
print(w)
