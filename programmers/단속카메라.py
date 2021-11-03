def solution(routes):
    answer = 1
    
    routes = sorted(routes, key=lambda x : x[1])    # 나가는 것 기준으로 정렬
    
    first, temp = routes[0]
    for a, b in routes:                             
        if temp < a:                                # 설치할 지점 전에 나가면 그 지점에 설치
            answer += 1
            temp = b
        
    return answer
