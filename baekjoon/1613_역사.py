import sys
input = sys.stdin.readline

# 파싱
n, k = map(int, input().split())
table = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    table[a][b] = 1

# 플로이드 워샬
for k in range(1, n + 1):
    for i in range(1, n + 1):
        if k == i or table[i][k] == 0:
            continue
        
        for j in range(1, n + 1):
            if table[i][k] and table[k][j]:
                table[i][j] = 1

# 쿼리 처리
s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    
    # a가 먼저 일어난 경우
    if table[a][b]:
        print(-1)
    # b가 먼저 일어난 경우
    elif table[b][a]:
        print(1)
    # 모르는 경우
    else:
        print(0)
