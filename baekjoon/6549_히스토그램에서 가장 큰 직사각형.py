import sys
input = sys.stdin.readline

while True:
    # 파싱
    nums = list(map(int, input().split()))
    n = nums.pop(0)
    # 탈출
    if n == 0:
        break
    
    # 넓이 계산
    answer = 0
    stack = []
    for i in range(n):
        # 작은 숫자는 전부 스택에서 방출
        while stack and nums[stack[-1]] > nums[i]:
            temp = stack.pop()
            
            # 스택의 마지막 숫자가 있는 곳 까지 자신보다 큰 숫자로 이루어짐
            # 그 사이의 넓이를 계산
            if stack:
                length = i - stack[-1] - 1
            # 없는 경우 자신이 지금까지의 숫자 중 가장 작은 것이기에 전부 체크
            else:
                length = i
            # 최댓값 반영
            answer = max(answer, length * nums[temp])
        
        # 현재 숫자 삽입
        stack.append(i)
    
    # 스택에 남아있는 것 방출
    while stack:
        temp = stack.pop()
        
        # 스택의 마지막 숫자가 있는 곳 까지 자신보다 큰 숫자로 이루어짐
        # 그 사이의 넓이를 계산
        if stack:
            length = n - stack[-1] - 1
        # 없는 경우 자신이 지금까지의 숫자 중 가장 작은 것이기에 전부 체크
        else:
            length = n
        # 최댓값 반영
        answer = max(answer, length * nums[temp])
    
    # 최댓값 출력
    print(answer)
