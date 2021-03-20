s = '>'+26*'1'+10*'2'+14*'3'
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>')
    if '>2' in s:
        s = s.replace('>2', '2>')
    if '>3' in s:
        s = s.replace('>3', '1>')
s = s.replace('>', '')
k = 0
for i in s:
    k+=int(i)
print(k)
