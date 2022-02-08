import sys
input = sys.stdin.readline

# 파싱
n = input().rstrip()
m = input().rstrip()
nlen, mlen = len(n), len(m)

# dp
dp = [["" for _ in range(mlen + 1)] for _ in range(nlen + 1)]
for i in range(nlen):
    for j in range(mlen):
        if n[i] == m[j]:
            dp[i + 1][j + 1] = dp[i][j] + n[i]
        else:
            if len(dp[i + 1][j]) > len(dp[i][j + 1]):
                dp[i + 1][j + 1] = dp[i + 1][j]
            else:
                dp[i + 1][j + 1] = dp[i][j + 1]

# 결과 출력
print(len(dp[nlen][mlen]))
print(dp[nlen][mlen])
