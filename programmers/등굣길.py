def solution(m, n, puddles):
    count = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    count[1][0] = 1                                                 # 시작 값 설정
    
    for x in range(1, n + 1):                                   
        for y in range(1, m + 1):
            if not [y, x] in puddles:
                count[x][y] = count[x - 1][y] + count[x][y - 1]     # 최단거리이기 때문에

    return count[n][m] % 1000000007
