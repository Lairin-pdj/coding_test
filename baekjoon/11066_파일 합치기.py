# pypy3로만 효율성 통과 코드

# 반복 횟수
n = int(input())

for _ in range(n):
    # 책의 수
    book = int(input())
    # 책의 페이지 수 리스트
    page = list(map(int, input().split()))

    # dp를 이용하여 풀이
    # dp[i][j] => i번째 책에서 j번째 책까지의 최소 값을 의미
    dp = [[0] * book for _ in range(book)]
    
    # 초기값 설정
    for j in range(book - 1):
        # 2권일 경우 경우의 수가 1가지
        dp[j][j + 1] = page[j] + page[j + 1]
        # 각 위치의 기본적인 값 설정
        # dp로는 합치는 것에 대한 값만 계산되므로 모든 책들이 1번씩은 계산되는 것을 포함시키게 하기 위함
        for k in range(j + 2, book):
            dp[j][k] = dp[j][k - 1] + page[k] 
    
    # 차례대로 최소값을 계산
    for j in range(2, book):
        for k in range(book - j):
            # 가능한 값들의 리스트 생성
            check = [dp[k][l] + dp[l + 1][k + j] for l in range(k, k + j)]
            # 최소값 대입
            dp[k][k + j] += min(check)

    print(dp[0][book - 1])
