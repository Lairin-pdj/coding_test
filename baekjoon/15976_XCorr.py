from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
y = [list(map(int, input().split())) for _ in range(m)]
a = int(input())
b = int(input())

# 투 포인터를 이용하여 범위 진행
j = 0
minheap = []
heaptotal = 0
answer = 0

# x 순차적으로 선택
for i in range(n):
    
    # heap에 가능한 만큼 삽입
    while j < m:
        if y[j][0] <= x[i][0] + b:
            heappush(minheap, y[j])
            heaptotal += y[j][1]
            j += 1
        else:
            break
    
    # heap에 범위 외 값 제거
    while minheap:
        if minheap[0][0] < x[i][0] + a:
            temp = heappop(minheap)
            heaptotal -= temp[1]
        else:
            break
    
    # 값 정산
    answer += x[i][1] * heaptotal

# 결과 출력
print(answer)
