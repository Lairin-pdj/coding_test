import sys
input = sys.stdin.readline

# 입력값 정리
n = int(input())
cases = []
for _ in range(n):
    cases.append(int(input()))

# 최댓값 저장
high = max(cases)

# 초기값 설정
dp = []
dp.append([1, 0])
dp.append([0, 1])

# dp계산
for i in range(2, high + 1):
    zero = dp[i - 1][0] + dp[i - 2][0]
    one = dp[i - 1][1] + dp[i - 2][1]
    dp.append([zero, one])

# 결과값 출력
for case in cases:
    print(" ".join(map(str, dp[case])))
