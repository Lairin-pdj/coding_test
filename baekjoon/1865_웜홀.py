from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
t = int(input())
for _ in range(t):
    n, m, w = map(int, input().split())
    table = defaultdict(defaultdict)
    for _ in range(m):
        s, e, t = map(int, input().split())
        
        if e not in table[s]:
            table[s][e] = t
        elif table[s][e] > t:
            table[s][e] = t
            
        if s not in table[e]:
            table[e][s] = t
        elif table[e][s] > t:
            table[e][s] = t
            
    for _ in range(w):
        s, e, t = map(int, input().split())
        
        if e not in table[s]:
            table[s][e] = -t
        elif table[s][e] > -t:
            table[s][e] = -t

    # 벨만포드
    dist = [1000000000] * (n + 1)
    dist[list(table.keys())[0]] = 0
    for i in range(n - 1):
        for i in table:
            for to in table[i]:
                if table[i][to] + dist[i] < dist[to]:
                    dist[to] = table[i][to] + dist[i]
    
    # 음수 사이클 체크
    cycle = False
    for i in table:
        for to in table[i]:
            if table[i][to] + dist[i] < dist[to]:
                cycle = True
    
    # 결과 출력
    if dist[list(table.keys())[0]] < 0 or cycle:
        print("YES")
    else:
        print("NO")
