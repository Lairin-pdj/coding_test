import sys
input = sys.stdin.readline

def matrix(x, y):
    # 반환 배열 초기화
    result = [[0 for _ in range(len(y[0]))] for _ in range(len(x))]
    
    # 곱셉 진행
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(x[0])):
                result[i][j] += x[i][k] * y[k][j]
    
    # 모드 적용
    for i in range(len(x)):
        for j in range(len(y[0])):
            result[i][j] %= 1000000007
    
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
n = int(input())

if n == 1:
    print(1)
else:
    # (f(n + 2)) = (1, 1)^ n + 1 (1)
    # (f(n + 1)) = (1, 0)        (0)
    a = [[1, 1], [1, 0]]
    b = [[1], [0]]

    # 결과 출력
    print(*matrix(power(a, n - 1), b)[0])
