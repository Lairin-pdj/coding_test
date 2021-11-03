def solution(n, results):
    # 결과를 저장하기 위한 배열 선언 및 초기화
    check = [[0 for _ in range(n)] for _ in range(n)]
    
    # 결과 값을 배열에 반영
    for a, b in results:
        check[a - 1][b - 1] = 1
        check[b - 1][a - 1] = -1
    
    # 결과 값들로 부터 승리를 유추할 수 있는 값들 체크
    # 연쇄가 필요한 부분을 위해 n번 더 반복
    for _ in range(n):                              
        for i in range(n):
            for j in range(n):
                if check[i][j] == 1:
                    for k in range(n):
                        if check[j][k] == 1:
                            check[i][k] = 1
                elif check[i][j] == -1:
                    for k in range(n):
                        if check[j][k] == -1:
                            check[i][k] = -1
    
    # 모든 결과가 유추 가능한 값들의 갯수 체크
    answer = 0
    for i in check:
        if i.count(0) == 1:
            answer += 1
            
    # 결과 값 출력        
    return answer
