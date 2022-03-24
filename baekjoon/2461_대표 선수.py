from collections import deque
import sys, heapq
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
nums = []
queue = []
# 정렬 후 삽입(n * mlogm)
for i in range(n):
    temp = list(map(int, input().split()))
    temp.sort()
    nums.append(deque(temp[1:]))
    heapq.heappush(queue, (temp[0], i))

# 순회
answer = 1000000000
high = max(queue)[0]
while queue:
    value, order = heapq.heappop(queue)
    
    # 결과 갱신
    answer = min(answer, high - value)
    
    # 뽑은 위치에서 다시 뽑기
    if nums[order]:
        temp = nums[order].popleft()
        high = max(high, temp)
        heapq.heappush(queue, (temp, order))
    # 한 쪽이 끝난 경우
    else:
        break
    
# 결과 출력
print(answer)
