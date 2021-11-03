from collections import deque

def hm2m(time):
    # str시간을 int분으로 치환해주는 함수  
    temp = time.split(":")
    return int(temp[0]) * 60 + int(temp[1])
    
def m2hm(time):
    # int분을 str시간으로 치환해주는 함수  
    hour = time // 60
    minute = time % 60
    return str(hour).zfill(2) + ":" + str(minute).zfill(2)

def solution(n, t, m, timetable):
    # 버스 시간표
    bus = []
    for i in range(n):
        bus.append(540 + i * t)
    
    # 크루 시간표
    crew = []
    for i in timetable:
        crew.append(hm2m(i))
        
    # 시간순으로 정렬
    crew.sort()
    
    # 빠른 출력을 위하여
    crew = deque(crew)
    
    # 버스를 기준으로 명수 체크
    # ready => 대기줄
    ready = deque()
    for i, time in enumerate(bus):
        # 버스의 시간 안에 도착한 크루 체크
        while crew and crew[0] <= time:
            ready.append(crew[0])
            crew.popleft()
            
        # 마지막 버스 체크
        if i == len(bus) - 1:
            if len(ready) < m:
                return m2hm(time)
            else:
                return m2hm(ready[m - 1] - 1)
            
        # 버스에 탈 수 있는만큼 버스에 태우기
        count = min(m, len(ready))
        for j in range(count):
            ready.popleft()
            
    # 에러 상황
    return -1
