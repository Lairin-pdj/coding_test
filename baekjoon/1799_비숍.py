import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000000)

# 파싱
n = int(input())
chessmap = [list(map(int, input().split())) for _ in range(n)]

# dfs 구현
def dfs(check, count):
    global bnt, wnt
    
    # 최종 탈출
    if count >= (2 * n - 1):
        if count % 2 == 1:
            bnt = max(bnt, len(check))
        else:
            wnt = max(wnt, len(check))
        return
    
    for i in range(count + 1):
        if 0 <= i < n and 0 <= count - i < n and chessmap[i][count-i] == 1:
            # 겹침 체크
            flag = True
            for j in range(1, min(i, count - i) + 1):
                if (i - j, count - i - j) in check:
                    flag = False
                    break
            
            if flag:
                check.add((i, count - i))
                dfs(check, count + 2)
                check.remove((i, count - i))
    
    # 해당 라인에 놓지 않은 경우 체크
    dfs(check, count + 2)

# dfs 실행
bnt, wnt = 0, 0
dfs(set(), 0)
dfs(set(), 1)

# 결과 출력
print(bnt + wnt)
