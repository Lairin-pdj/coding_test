import sys, heapq
input = sys.stdin.readline
    
# 파싱
k, n = map(int, input().split())
nums = list(map(int, input().split()))

# 형태 변환
check = nums[:]
heapq.heapify(check)

# n번 추출
answer = 0
for _ in range(n):
    answer = heapq.heappop(check)

    for j in nums:
        heapq.heappush(check, answer * j)
        if answer % j == 0:
            break

# 결과 출력
print(answer)
