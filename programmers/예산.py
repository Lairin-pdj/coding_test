def solution(d, budget):
    answer = 0
    
    # 최대 지원 부서 수를 구하는 것이기 때문에
    # 최소 비용 부서부터 처리하기 위해 정렬
    d.sort()
    
    # 지원 가능 부서 여부 판단 및 체크
    for i in d:
        if budget - i >= 0:
            answer += 1
            budget -= i
        else:
            break
    
    return answer
