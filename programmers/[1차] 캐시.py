from collections import deque

def solution(cacheSize, cities):
    # 캐시 사이즈가 0일 경우
    if cacheSize == 0:
        return len(cities) * 5
    
    # 실행시간
    answer = 0
    # 캐시 공간
    cache = deque()
    
    # 도시 방문 순서대로 체크
    for city in cities:
        # 대소문자 구분하지 않기 위해
        city = city.lower()
        
        # hit
        if city in cache:
            answer += 1
            # 맨 뒤로 이동
            cache.remove(city)
            cache.append(city)
            
        # miss
        else:
            answer += 5
            # 맨 뒤에 넣는데 크기가 초과하면 맨 앞 제거
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.popleft()
                cache.append(city)
        
    return answer
