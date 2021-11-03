import sys
input = sys.stdin.readline

# 입력 파싱
n = int(input())
cases = []
for _ in range(n):
    cases.append(int(input()))

# dp 배열 생성
high = max(cases)
dp = [0] * (high + 1)

# 초기값 설정
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

# 순차 진행
for i in range(6, high + 1):
    dp[i] = dp[i - 1] + dp[i - 5]
    
# 결과값 출력
for case in cases:
    print(dp[case])
