import heapq

def solution(jobs):
    answer = 0

    count = 1
    jobs.sort()                                                 # 시간 순서대로 정렬
    temp = []
    for a, b in jobs:                                           # 우선순위큐를 사용하기 위해 뒤집음 
        temp.append([b, a])
    jobs = temp
    
    queue = []
    heapq.heappush(queue, jobs[0])                              # 맨 처음 작업을 진행
    time = jobs[0][1]                                           # 작업한 뒤 시간을 측정
    
    while len(queue) > 0:                                       # 모든 작업이 마무리 될때 까지 반복
        temp = heapq.heappop(queue)                             # 현재 큐 중 가장 짧은 작업 진행 및 시간 추가
        time += temp[0]                                         
        answer += (time - temp[1])
        while count < len(jobs) and jobs[count][1] <= time:     # 현재 시간에 요청이 온 작업들 큐에 삽입
            heapq.heappush(queue, jobs[count])
            count += 1
        if count < len(jobs) and len(queue) == 0:               # 큐를 다 소진하고 요청또한 없을 경우 다음 요청까지 건너뛰기
            heapq.heappush(queue, jobs[count])
            time = jobs[count][1]
            count += 1
            
    return int(answer / len(jobs))                              # 결과값 반환
