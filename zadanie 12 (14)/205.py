w = '1' * 2019 + '3' * 2019
while '111' in w:
    w = w.replace('111', '2', 1)
    w = w.replace('222', '3', 1)
    w = w.replace('333', '1', 1)
print(w)