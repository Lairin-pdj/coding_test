from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 파싱
t = int(input())
for _ in range(t):
    dic = defaultdict(list)
    n = int(input())
    table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    check = [0] * (n + 1)
    
    # 기존 정보 간선
    before = list(map(int, input().split()))
    for i in range(n - 1):
        for j in range(i + 1, n):
            table[before[i]][before[j]] = 1
            table[before[j]][before[i]] = -1
    
    # 올해 간선 정보로 수정
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if table[a][b] == 1:
            table[a][b] = -1
            table[b][a] = 1
        else:
            table[a][b] = 1
            table[b][a] = -1

    # 간선 최종 적용
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if table[i][j] == 1:
                dic[i].append(j)
                check[j] += 1
    
    # 위상정렬
    # 시작 가능 지점 체크 및 큐에 삽입
    queue = deque()
    for i in range(1, n + 1):
        if check[i] == 0:
            queue.append(i)

    # 정점 진행
    answer = []
    while queue:
        now = queue.popleft()
        answer.append(now)
        
        for i in dic[now]:
            if check[i] == 1:
                check[i] = 0
                queue.append(i)
            else:
                check[i] -= 1

    # 결과 출력
    if len(answer) != n:
        print("IMPOSSIBLE")
    else:
        print(*answer)
