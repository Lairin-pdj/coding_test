import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)                             # 우선순위 큐 사용
    
    while len(scoville) > 1:                            # 1개만 남을 때까지 반복
        if scoville[0] >= K:                            # 다 하기 전 조건 만족시 탈출
            break
            
        temp1 = heapq.heappop(scoville)                 # 맵지 않은 두개 추출
        temp2 = heapq.heappop(scoville)
        
        heapq.heappush(scoville, temp1 + (temp2 * 2))   # 합쳐서 다시 큐에 삽입
        answer += 1
            
    if len(scoville) == 1:                              # 결과 체크 
        if scoville[0] < K:
            answer = -1

    return answer
