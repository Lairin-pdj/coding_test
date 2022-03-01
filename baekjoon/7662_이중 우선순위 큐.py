from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

# 파싱
t = int(input())
for _ in range(t):
    n = int(input())
    high, low = [], []
    check = defaultdict(int)
    count = 0
    
    # 쿼리 처리
    for _ in range(n):
        op, num = input().split()
        num = int(num)
        
        if op == "I":
            heapq.heappush(low, num)
            heapq.heappush(high, -num)
            check[num] += 1
            count += 1
        else:
            if count > 0:
                if num == -1:
                    temp = heapq.heappop(low)
                    while check[temp] == 0:
                        temp = heapq.heappop(low)
                    check[temp] -= 1
                else:
                    temp = -heapq.heappop(high)
                    while check[temp] == 0:
                        temp = -heapq.heappop(high)
                    check[temp] -= 1
                count -= 1
    
    # 최소, 최대 출력
    if count > 0:
        # 최대
        temp = -heapq.heappop(high)
        while check[temp] == 0:
            temp = -heapq.heappop(high)
        print(temp, end = " ")
        
        # 최소
        temp = heapq.heappop(low)
        while check[temp] == 0:
            temp = heapq.heappop(low)
        print(temp)
        
    # 빈 경우
    else:
        print("EMPTY")
