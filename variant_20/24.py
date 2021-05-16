import sys
file = open(file='Задание 24/24.txt')
sys.stdin = file

mk = 0
st = ''
s = list(map(len, input().split("XZZY")))
for i in range(len(s)):
    s[i]+=6
s[0] -= 3
s[-1] -= 3
print(max(s))
