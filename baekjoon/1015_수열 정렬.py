import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))

# 위치 저장
check = []
for i in range(n):
    check.append([nums[i], i])

# 정렬 후 순서 정보 저장
check.sort()
for i in range(n):
    check[i][0] = i

# 재정렬 후 출력
check.sort(key = lambda x : (x[1]))
print(*list(zip(*check))[0])
