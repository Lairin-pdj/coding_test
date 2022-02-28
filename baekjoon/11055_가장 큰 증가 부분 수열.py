import sys
input = sys.stdin.readline

# 파싱
n = int(input())
lines = [0] + list(map(int, input().split()))

# dp
dp = [0 for _ in range(n + 1)]
dp[0], answer = lines[0], lines[0]
for i in range(1, n + 1):
    for j in range(i):
        if lines[j] < lines[i]:
            dp[i] = max(dp[i], dp[j] + lines[i])
            answer = max(answer, dp[i])

# 결과 출력
print(answer)
