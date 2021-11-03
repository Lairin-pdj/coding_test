import sys
input = sys.stdin.readline

# 입력 파싱
n = int(input())

# dp배열 생성
dp = [[0] * 10 for _ in range(n + 1)]

# 초기값 설정
dp[1] = [0] + [1] * 9

# dp 진행
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
    
# 결과값 출력
print(sum(dp[n]) % 1000000000)
