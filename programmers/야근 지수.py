import heapq

def solution(n, works):
    amount = sum(works)
    quantity = len(works)
    
    # 야근을 하지 않아도 되는 경우
    if amount < n:
        return 0
    
    # 피로도는 제곱이기 때문에 골고루 줄여주는 것이 필요
    # 최대힙 활용
    heap = []
    for i in works:
        heapq.heappush(heap, (-i, i))
    
    # n번 숫자를 줄여줌
    for _ in range(n):
        a, b = heapq.heappop(heap)
        b -= 1
        heapq.heappush(heap, (-b, b))
    
    # 제곱값 계산
    answer = 0
    for a, b in heap:
        answer += b ** 2
    
    # 결과값 반환
    return answer
