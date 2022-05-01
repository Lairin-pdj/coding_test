import sys
input = sys.stdin.readline

# 파싱
n = int(input())

# 순차적 체크
answer = 0
stack = []
for _ in range(n):
    a = int(input())
    
    # 이미 볼수 없는 아이 제거
    while stack:
        if stack[-1][0] < a:
            # 현재 들어온 사람과 조합 후 추가적인 조합 불가능
            answer += stack[-1][1]
            stack.pop()
        else:
            break
    
    # 가능한 조합수 체크
    if stack: 
        if stack[-1][0] == a:
            answer += stack[-1][1]
            if len(stack) >= 2:
                answer += 1
        else:
            answer += 1

    # 스택에 추가
    if stack and stack[-1][0] == a:
        stack[-1][1] += 1
    else:
        stack.append([a, 1])

# 결과 출력
print(answer)
