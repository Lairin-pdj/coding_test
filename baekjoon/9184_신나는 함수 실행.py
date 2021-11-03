import sys
input = sys.stdin.readline

cases = []

# 무한 반복
while True:
    # 파싱
    a, b, c = map(int, input().split(" "))
    
    # 탈출 조건
    if a == -1 and b == -1 and c == -1:
        break

    cases.append([a, b, c])
    
# dp 배열 선언
dp = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

# dp 실행
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i < j and j < k:
                dp[i][j][k] = dp[i][j][k - 1] + dp[i][j - 1][k - 1] - dp[i][j - 1][k]
            else:
                dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1]
    
# 결과값 출력
for a, b, c in cases:
    # 하나라도 0이하면 바로 1
    if a <= 0 or b <= 0 or c <= 0:
        print("w({}, {}, {}) = {}".format(a, b, c, 1))
    elif a > 20 or b > 20 or c > 20:
        # a, b, c는 보존
        print("w({}, {}, {}) = {}".format(a, b, c, dp[20][20][20]))
    else:
        print("w({}, {}, {}) = {}".format(a, b, c, dp[a][b][c]))
