import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))
check = [0] * 1000001
for i in nums:
    check[i] += 1

# 스택 활용 순회
stack = []
answer = [-1] * n
for i in range(n):
    
    # 판단 가능한 수 처리
    while stack:
        if check[nums[stack[-1]]] < check[nums[i]]:
            order = stack.pop()
            answer[order] = nums[i]
        else:
            break
    
    # 현재 수 넣기
    stack.append(i)

# 결과 출력
print(*answer)
