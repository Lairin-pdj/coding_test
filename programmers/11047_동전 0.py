import sys
input = sys.stdin.readline

n, k = map(int, input().split(" "))

# 코인을 내림차순으로 정리
coins = [int(input()) for _ in range(n)]
coins = coins[::-1]

# 그리디방식으로 비싼코인이 가능한 갯수 체크
count = 0
for coin in coins:
    if k == 0:
        break
    count += k // coin
    k = k % coin
    
print(count)
