import sys
input = sys.stdin.readline
inf = float('inf')

# 파싱
n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]

# 플로이드 워샬로 갱신 체크
flag = False
for k in range(n):
    for i in range(n):
        if i == k:
            continue
        for j in range(n):
            if k == j or i == j:
                continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                flag = True
                break
        
        if flag:
            break
        
    if flag:
        break

# 가능한 거리표 였을 경우
if not flag:
    # 플로이드 워샬 역추척
    for k in range(n):
        for i in range(n):
            if i == k:
                continue
            for j in range(n):
                if k == j or i > j:
                    continue
                if dist[i][j] == dist[i][k] + dist[k][j]:
                    dist[i][j] = inf
                    dist[j][i] = inf

    # 결과 계산
    answer = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if dist[i][j] != inf:
                answer += dist[i][j]
    
    # 결과 출력
    print(answer)
    
# 갱신이 발생한 경우
else:
    print(-1)
