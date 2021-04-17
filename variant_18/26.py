import sys
sys.stdin = open(file='Задание 26/26.txt')
n = int(input())
arr_200plus = []
arr_200minus = []
for i in range(n):
    x = int(input())
    if x <= 200:
        arr_200minus.append(x)
    else:
        arr_200plus.append(x)
arr_200plus.sort()
print(arr_200plus)
skid=sum(arr_200plus[:len(arr_200plus)//2])*0.3
stoimsoskid=sum(arr_200plus) + sum(arr_200minus) - skid
print(stoimsoskid)
print(arr_200plus[len(arr_200plus)//2-1])