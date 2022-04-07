import sys, heapq
input = sys.stdin.readline
    
# 파싱
n = int(input())
works = [[] for _ in range(1001)]
end = 0
for _ in range(n):
    d, w = map(int, input().split())
    end = max(end, d)
    works[d].append(w)

# 역 순으로 과제 수행
answer = 0
queue = []
day = end
while day > 0:
    
    # 당일 마감되는 일 큐에 삽입
    for work in works[day]:
        heapq.heappush(queue, -work)
    
    # 가장 큰 값 수행
    if queue:
        w = heapq.heappop(queue)
        answer += -w

    day -= 1

# 결과 출력
print(answer)
