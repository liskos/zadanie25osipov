def func(x):
    if x == 'л':
        return 0
    elif x == 'и':
        return func('л') + 1
    elif x == 'к':
        return func('л') + 1
    elif x == 'е':
        return max(func('и'), func('л')) + 1
    elif x == 'д':
        return max(func('и'), func('е')) + 1
    elif x == 'ж':
        return max(func('е'), func('к'), func('л')) + 1
    elif x == 'б':
        return func('д') + 1
    elif x == 'г':
        return func('ж') + 1
    elif x == 'в':
        return max(func('б'), func('д'), func('ж'), func('г')) + 1
    elif x == 'а':
        return max(func('б'), func('в'), func('г')) + 1


print(func('а'))
