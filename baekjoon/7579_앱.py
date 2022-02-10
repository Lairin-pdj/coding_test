import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
high = sum(cost)

# 냅색
dp = [[0 for _ in range(high + 1)] for _ in range(n + 1)]
answer = high
for i in range(1, n + 1):
    for j in range(high + 1):
        if cost[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - cost[i]] + memory[i], dp[i - 1][j])
        
        # 만족 체크
        if dp[i][j] >= m:
            answer = min(answer, j)
            break

# 결과 출력
print(answer)
