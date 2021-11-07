import sys
input = sys.stdin.readline

# 파싱
n = int(input())
dist = list(map(int, input().split()))
citys = list(map(int, input().split()))

price = 1000000000
tdist, count = 0, 0
for i in range(n - 1):
    if price > citys[i]:
        count += price * tdist
        price = citys[i]
        tdist = dist[i]
    else:
        tdist += dist[i]

print(count + tdist * price)
