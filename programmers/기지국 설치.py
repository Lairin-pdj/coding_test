import math

def solution(n, stations, w):
    answer = 0
    # 기지국의 전파 범위
    wide = 2 * w + 1
    
    # 기존 기지국이 없는 경우 
    if len(stations) == 0:
        # 기지국의 전파 범위로 올림 
        return math.ceil(n / wide)
    
    # 기지국을 정렬
    stations.sort()
    
    now = 0
    # 기존의 기지국으로 커버하지 못하는 부분을 탐색
    for i in stations:
        # 커버하지 못하는 만큼 기지국 갯수 추가
        answer += math.ceil((i - w - 1 - now) / wide)
        now = i + w
    
    # 맨 마지막 커버 범위 이후 부분 처리
    if now < n:
        answer += math.ceil((n - now) / wide)

    return answer
