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

    # 결과 반환
    return result

# 파싱
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

# 결과 출력
for i in matrix(a, b):
    print(*i)
