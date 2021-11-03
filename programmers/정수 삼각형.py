def solution(triangle):
    answer = 0
    
    for i in range(1, len(triangle)):                                                 # 모든 값을 순회
        for j in range(len(triangle[i])):                       
            if j == 0:                                                                # 좌 상단 값이 없는 경우
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:                                           # 우 상단 값이 없는 경우
                triangle[i][j] += triangle[i - 1][j - 1]
            else:                                                                     # 둘 다 있는 경우
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
            
    for i in triangle[-1]:
        answer = max(answer, i)                                                       # 최댓값 체크
    
    return answer
