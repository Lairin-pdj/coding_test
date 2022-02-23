import sys
input = sys.stdin.readline

# 파싱
n, l, k = map(int, input().split())

# dp
dp = [[1 for _ in range(l + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, l + 1):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

# k번째 생성
answer = ""
count = 0
origin = n
while count < origin:
    # 남은 1이 없는 경우 0 채우기 반복
    if l == 0:
        if count < origin:
            answer += "0" * (origin - count)
            break
    elif n == l:
        count += 1
        n -= 1
        l -= 1
        if dp[n][l] < k:
            k -= dp[n][l]
            answer += "1"
        else:
            answer += "0"
    else:
        count += 1
        n -= 1
        if dp[n][l] < k:
            k -= dp[n][l]
            l -= 1
            answer += "1"
        else:
            answer += "0"

# 결과 출력
print(answer)
