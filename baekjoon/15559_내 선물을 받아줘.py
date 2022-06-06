import sys
input = sys.stdin.readline
    
# 파싱
n, m = map(int, input().split())
table = [input().rstrip() for _ in range(n)]
direct = {"N": (-1, 0), "W": (0, -1), "E": (0, 1), "S": (1, 0)}

# dfs
visited = [[0 for _ in range(m)] for _ in range(n)]
group = 1
answer = 0
# 전부 순회
for i in range(n):
    for j in range(m):
        # 이미 방문한 경우
        if visited[i][j]:
            continue
        
        # 좌표 이동
        ai, aj = i, j 
        while not visited[ai][aj]:
            visited[ai][aj] = group
            ai += temp[0]
            aj += temp[1]
        
        # 선물 장소로 판단
        if visited[ai][aj] == group:
            answer += 1
            
        group += 1

# 결과 출력
print(answer)
