import sys
sys.stdin = open(file='26data/26-k1.txt')
n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort(reverse=True)
print('ценa самого дорогого товара, не участвующего в распродаже', a[k])
print('целая часть от суммы всех скидок', int(0.2 * sum(a[:k])))