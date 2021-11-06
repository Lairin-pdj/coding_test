import sys, heapq
input = sys.stdin.readline

# 파싱
n = int(input())

# leftmax + rightmin => 정렬
# leftmax의 최대값이 문제에서 요구한 중간값
rightmin = []
leftmax = []
for _ in range(n):
    num = int(input())
    
    if len(leftmax) > len(rightmin):
        heapq.heappush(rightmin, num)
    else:
        heapq.heappush(leftmax, -num)
    
    # 들어간 수가 다른 한쪽의 값보다 작거나 큰 경우 방지
    if rightmin and -leftmax[0] > rightmin[0]:
        a = heapq.heappop(leftmax)
        b = heapq.heappop(rightmin)
        heapq.heappush(leftmax, -b)
        heapq.heappush(rightmin, -a)
        
    print(-leftmax[0])
