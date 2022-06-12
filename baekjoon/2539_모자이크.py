import sys
input = sys.stdin.readline
    
# 파싱
n, m = map(int, input().split())
paper = int(input())
h = int(input())
holes = [list(map(int, input().split())) for _ in range(h)]

# 최소 높이 탐색
minimum = 0
for a, b in holes:
    minimum = max(minimum, a)
    
# 정렬
holes.sort(key = lambda x : x[1])

# 이분탐색
answer = 0
low = minimum
high = max(n, m)
while low <= high:
    mid = (low + high) // 2
    
    # 가능한지 체크
    flag = False
    check, count, j = 0, 0, 0
    while count <= paper:
        
        # 이미 다 채운 경우
        if j >= h:
            flag = True
            break
        
        # 이미 넘치는 경우
        if count == paper:
            break
        
        # mid 만큼 진행
        check = holes[j][1] + mid - 1
        while j < h and check >= holes[j][1]:
            j += 1
        
        count += 1
    
    # 결과 여부에 따른 처리
    if flag:
        high = mid - 1
        answer = mid
    else:
        low = mid + 1

# 결과 출력
print(answer)
