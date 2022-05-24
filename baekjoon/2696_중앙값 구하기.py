from math import ceil
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# 파싱
t = int(input())
for _ in range(t):
    m = int(input())
    nums = []
    for _ in range(ceil(m / 10)):
        nums += list(map(int, input().split()))
    
    # left = maxheap, right = minheap
    left, right = [], []
    answer = [nums[0]]
    mid = nums[0]
    
    for i in range(1, len(nums), 2):
        if nums[i] >= answer[-1]:
            heappush(right, nums[i])
        else:
            heappush(left, -nums[i])
        if nums[i + 1] >= answer[-1]:
            heappush(right, nums[i + 1])
        else:
            heappush(left, -nums[i + 1])
            
        # 갯수 체크를 통한 중간값 변경
        if len(left) < len(right):
            heappush(left, -mid)
            mid = heappop(right)
        elif len(left) > len(right):
            heappush(right, mid)
            mid = -heappop(left)
        
        # 중간값 answer에 추가
        answer.append(mid)
    
    # 결과 출력
    print(len(answer))
    for i in range(len(answer)):
        if i != 0 and i % 10 == 0:
            print()
        print(answer[i], end = " ")
    print()
