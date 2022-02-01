from collections import deque
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
chu = list(map(int, input().split()))
t = int(input())
nums = list(map(int, input().split()))

# 체크표
high = max(nums) + 1
check = [False for _ in range(high)]
can = set()
queue = deque()
queue.append([0, 0])
while queue:
    x, i = queue.popleft()

    if (x, i) not in can:
        can.add((x, i))
        
        if 0 <= x < high:
            check[x] = True
        
        for j in range(i, n):
            queue.append([x + chu[j], j + 1])
            queue.append([x - chu[j], j + 1])
    

# 결과 출력
for i in nums:
    if check[i]:
        print("Y", end = " ")
    else:
        print("N", end = " ")
