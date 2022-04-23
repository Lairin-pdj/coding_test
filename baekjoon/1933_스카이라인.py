from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

# 파싱
n = int(input())
dic = defaultdict(list)
for _ in range(n):
    l, h, r = map(int, input().split())
    dic[l].append(h)
    dic[r].append(-h)

# 변화 기록
temp = list(dic.keys())
temp.sort()
check = defaultdict(int)
queue = []
high = 0
for now in temp:
    
    # 변화 큐에 삽입
    for i in dic[now]:
        if i > 0:
            heapq.heappush(queue, -i)
            check[i] += 1
        else:
            check[-i] -= 1
            if check[-i] == 0:
                del check[-i]
    
    # 헛값 제거
    while queue and -queue[0] not in check:
        heapq.heappop(queue)
    
    # 변화 감지
    if queue:
        if -queue[0] != high:
            print(now, -queue[0], end = " ")
            high = -queue[0]
    else:
        print(now, 0, end = " ")
        high = 0
