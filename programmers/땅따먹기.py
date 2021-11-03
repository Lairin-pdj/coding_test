def solution(land):
    # 동적계획법 사용
    dp = [[0, 0, 0, 0] for _ in range(len(land))]
    dp[0] = land[0]
    
    # 각 위치를 밟을 경우의 최대값을 계산
    for i in range(1, len(land)):
        for j in range(4):
            if j == 0:
                dp[i][j] = max(dp[i - 1][1], dp[i - 1][2], dp[i - 1][3]) + land[i][j]
            elif j == 1:
                dp[i][j] = max(dp[i - 1][0], dp[i - 1][2], dp[i - 1][3]) + land[i][j]
            elif j == 2:
                dp[i][j] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][3]) + land[i][j]
            else:
                dp[i][j] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]) + land[i][j]
    
    # 맨 마지막 층의 최대값 반환
    return max(dp[len(land) - 1])
