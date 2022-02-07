from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 파싱
t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    dic = defaultdict(list)
    for _ in range(e):
        a, b = map(int, input().split())
        dic[a].append(b)
        dic[b].append(a)
    
    # 이분 그래프 체크
    flag = True
    visit = [False for _ in range(v + 1)]
    
    # 연결그래프가 아닐 경우를 상정해 모든 정점 체크
    for i in range(1, v + 1):
        if not visit[i]:
            visit[i] = True
            check = set([(i, 1)])
            queue = deque([(i, 1)])
            while queue:
                n, c = queue.popleft()
                
                # 연결된 다른 곳으로 이동
                for j in dic[n]:
                    if (j, c) in check:
                        flag = False
                        break
                    elif (j, -c) not in check:
                        visit[j] = True
                        check.add((j, -c))
                        queue.append((j, -c))
                
                # 이미 조건을 만족하지 못할 경우 탈출
                if not flag:
                    break
            
            # 이미 조건을 만족하지 못할 경우 탈출
            if not flag:
                break

    # 결과 출력
    if flag:
        print("YES")
    else:
        print("NO")
