w = '1' * 2018 + '2' * 2019
while '111' in w:
    w = w.replace('111', '2', 1)
    w = w.replace('222', '1', 1)
print(w)
