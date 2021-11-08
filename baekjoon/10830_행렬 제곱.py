import sys
input = sys.stdin.readline

def matrix(x, y):
    # 반환 배열 초기화
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    # 곱셉 진행
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += x[i][k] * y[k][j]
    
    # 모드 적용
    for i in range(n):
        for j in range(n):
            result[i][j] %= 1000
    
    # 결과 반환
    return result

def power(a, b):
    # 제곱 단위를 분해하여 계산
    if b == 1:
        return a
    elif b % 2 == 0:
        temp = power(a, b // 2)
        return matrix(temp, temp)
    else:
        temp = power(a, b // 2)
        return matrix(matrix(temp, temp), a)

# 파싱
n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 결과 행렬 체크
answer = power(a, b)
for i in range(n):
    for j in range(n):
        answer[i][j] %= 1000

# 결과 출력
for i in answer:
    print(*i)
