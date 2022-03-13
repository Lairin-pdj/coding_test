import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))
s = int(input())

# 소트
count = 0
for i in range(n - 1):
    # 이동가능한 거리 만큼 최대값 탐색
    dist = 0
    temp, point = nums[i], -1
    for j in range(i + 1, n):
        if count + dist < s:
            dist += 1
            if nums[j] > temp:
                temp = nums[j]
                point = j
        else:
            break
    
    # 찾은 경우 수정
    if point != -1:
        count += point - i
        nums = nums[:i] + nums[point:point + 1] + nums[i:point] + nums[point + 1:]
    
    # 다 쓴 경우 탈출
    if count >= s:
        break

# 결과 출력
print(*nums)
