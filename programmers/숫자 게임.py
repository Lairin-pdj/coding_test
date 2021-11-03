def solution(A, B):
    answer = 0
    
    # 순서대로 비교하기 위해 정렬
    A.sort()
    B.sort()
    
    limit = len(A)
    i, j = 0, 0
    while j < limit:
        # b가 큰 경우만 체크  
        if A[i] < B[j]:
            answer += 1
            i += 1
        j += 1
    
    return answer
