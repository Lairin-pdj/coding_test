import math

def promise(depth, line, n, k):
    # 현재 위치가 놓을 수 있는 위치인지 체크
    for i in range(depth):
        if k == line[i] or depth - i == abs(k - line[i]):
            return False
    
    return True

def n_queen(depth, line, n):
    global answer
    if depth == n:
        answer += 1
        return
    
    # (depth, 0) ~ (depth, n - 1)까지 체크 후 백트래킹 진행
    for i in range(n):
        if promise(depth, line, n, i):
            # 가능한 경우 적용 후 다음 깊이로 진행
            line[depth] = i
            n_queen(depth + 1, line, n)
    
def solution(n):
    global answer
    answer = 0
    
    line = [-1 for _ in range(n)]
    
    # 깊이 0부터 시작
    n_queen(0, line, n)
    
    return answer
