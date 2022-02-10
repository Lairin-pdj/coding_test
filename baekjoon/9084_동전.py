import sys
input = sys.stdin.readline

# 파싱
t = int(input())
for _ in range(t):
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    
    # dp
    dp = [1] + [0 for _ in range(m)]
    for c in coin:
        for i in range(c, m + 1):
            if i - c >= 0:
                dp[i] += dp[i - c]
    
    # 결과 출력
    print(dp[m])
