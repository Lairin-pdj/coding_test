def solution(rows, columns, queries):
    answer = []
    
    matrix = []
    for i in range(1, rows * columns + 1):                          # 초기 행렬 초기화
        matrix.append(i)
        
    for a, b, c, d in queries:
        small = 10000                                               # 최솟값 체크
        temp = [[], [], [], []]                                 
        for i in range(b, d):                                       # 주어진 범위의 변을 각 각 임시 저장
            temp[0].append(matrix[columns * (a - 1) + i - 1])
            small = min(small, matrix[columns * (a - 1) + i - 1])
        for i in range(d, b, -1):
            temp[1].append(matrix[columns * (c - 1) + i - 1])
            small = min(small, matrix[columns * (c - 1) + i - 1])
        for i in range(a, c):
            temp[2].append(matrix[columns * (i - 1) + d - 1])
            small = min(small, matrix[columns * (i - 1) + d - 1])
        for i in range(c, a, -1):
            temp[3].append(matrix[columns * (i - 1) + b - 1])
            small = min(small, matrix[columns * (i - 1) + b - 1])
            
        for i in range(b, d):                                       # 행렬에 적용
            matrix[columns * (a - 1) + i] = temp[0][i - b]
        for i in range(d, b, -1):
            matrix[columns * (c - 1) + i - 2] = temp[1][d - i]
        for i in range(a, c):
            matrix[columns * (i) + d - 1] = temp[2][i - a]
        for i in range(c, a, -1):
            matrix[columns * (i - 2) + b - 1] = temp[3][c - i]

        answer.append(small)                                        
        
    return answer
