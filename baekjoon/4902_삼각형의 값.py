import sys
input = sys.stdin.readline

# 파싱
count = 1
while True:
    nums = list(map(int, input().split()))
    n = nums[0]
    
    # 종료
    if n == 0:
        break
    
    # 세팅
    table = [[0] * (2 * n) for _ in range(n)]
    
    # 누적합
    k = 1
    for i in range(n):
        for j in range(2 * i + 1):
            table[i][j] = nums[k] + table[i][j - 1]
            k += 1
    
    # 정방향 삼각형
    answer = -1000
    for i in range(n):
        for j in range(0, 2 * i + 1, 2):
            temp = 0
            for k in range(n - i):
                temp += table[i + k][j + 2 * k] - table[i + k][j - 1]
                answer = max(answer, temp)
    
    # 역방향 삼각형
    for i in range(n - 1, 0, -1):
        for j in range(1, 2 * i + 1, 2):
            temp = 0
            for k in range(min((j // 2) + 1, ((2 * i - j) // 2) + 1)):
                temp += table[i - k][j] - table[i - k][j - 2 * k - 1]
                answer = max(answer, temp)
    
    # 결과 출력
    print(f'{count}. {answer}')
    count += 1
