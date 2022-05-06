import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

# 가능한 수 탐색
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
def dfs(x, y):
    global ycount
    
    # 탈출 조건
    if len(stack) == 7 and ycount < 4:
        answer.add(tuple(sorted(stack)))
        return
    
    # 이미 확인 해본 케이스 탈출
    if tuple(sorted(stack)) in check:
        return
    
    # 전파가능 리스트 생성
    can = set()
    for sx, sy in stack:
        for i in range(4):
            can.add((sx + dx[i], sy + dy[i]))
    
    # 전파
    for ax, ay in can:    
        if 0 <= ax < 5 and 0 <= ay < 5 and (ax, ay) not in stack:
            # 불가능한 케이스 제거 
            if ycount >= 4:
                return
            
            stack.append((ax, ay))
            if table[ax][ay] == "Y":
                ycount += 1
            dfs(ax, ay)
            px, py = stack.pop()
            if table[px][py] == "Y":
                ycount -= 1
    
    # 완벽 확인이 끝난 조 체크
    check.add(tuple(sorted(stack)))

# 파싱
table = [input().rstrip() for _ in range(5)]

# 순회 dfs
stack = []
check = set()
ycount = 0
answer = set()
for i in range(5):
    for j in range(5):
        stack.append((i, j))
        if table[i][j] == "Y":
            ycount += 1
        dfs(i, j)
        px, py = stack.pop()
        if table[px][py] == "Y":
            ycount -= 1

# 결과 출력
print(len(answer))
