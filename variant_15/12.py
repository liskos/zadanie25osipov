s = '>' + 100 * '432' + '<'
while '>4' in s or '>3' in s or '>2' in s or '4<' in s or '3<' in s or '2<' in s:
    if '>4' in s or '>3' in s:
        s = s.replace('>4', '2>3')
        s = s.replace('>3', '1>2')
    elif '4<' in s or '3<' in s:
        s = s.replace('4<', '3<2')
        s = s.replace('3<', '2<1')
    else:
        s = s.replace('>2', '0>')
        s = s.replace('2<', '<0')
s = s.replace('>', '')
s = s.replace('<', '')
k = 0
for i in s:
    k += int(i)
print(k)
