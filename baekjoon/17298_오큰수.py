import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))

# 정답 배열
answer = [-1 for _ in range(n)]
stack = []

# 큰수가 들어오는지 체크
for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        answer[stack.pop()] = nums[i]
    stack.append(i)

# 답안 출력
print(*answer)
