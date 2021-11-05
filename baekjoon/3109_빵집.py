import sys
input = sys.stdin.readline

def dfs(x, y):
    global count, check
    
    # 도착한 경우
    if y == c - 1:
        count += 1
        return True
        
    temp = False
    
    # 가능한 위쪽으로 연결
    if x - 1 >= 0 and pipemap[x - 1][y + 1] == "." and check[x - 1][y + 1] == 0:
        check[x - 1][y + 1] = 1
        temp = dfs(x - 1, y + 1)

    if not temp and pipemap[x][y + 1] == "." and check[x][y + 1] == 0:
        check[x][y + 1] = 1
        temp = dfs(x, y + 1)

    if not temp and x + 1 < r and pipemap[x + 1][y + 1] == "." and check[x + 1][y + 1] == 0:
        check[x + 1][y + 1] = 1
        temp = dfs(x + 1, y + 1)
        
    return temp

# 파싱
r, c = map(int, input().split())
pipemap = [list(input().rstrip()) for _ in range(r)]

# 체크용 메모리 확보
count = 0
check = [[0 for _ in range(c)] for _ in range(r)]

# dfs 그리디 
for i in range(r):
    dfs(i, 0)

# 결과 출력
print(count)
