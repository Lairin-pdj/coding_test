import sys, heapq
input = sys.stdin.readline

# 파싱
n = int(input())

lines = []
for _ in range(n):
    a, b = map(int, input().split())
    if a < b:
        lines.append([a, b])
    else:
        lines.append([b, a])
        
lines.sort(key = lambda x : (x[1], x[0]))

d = int(input())

# 스위핑
answer = 0
now = []
end = lines[0][1]
start = end - d

# 라인별로 체크
for a, b in lines:
    
    # d보다 길이가 짧은 것만 체크
    if b - a <= d:
        
        # 삽입
        heapq.heappush(now, a)
        
        # 끝점을 기준으로 초과하면 이동
        if b > end:
            end = b
            start = end - d
            
            # 이동하며 제외되는 부분 제거
            while now:
                if now[0] < start:
                    heapq.heappop(now)
                else:
                    break
        
        # 최댓값 반영
        answer = max(answer, len(now))

# 결과출력
print(answer)
