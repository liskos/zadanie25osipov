print(sum([1 for i in open(file='24/24.txt', mode='r') if i.count('E') > i.count('A')]))
