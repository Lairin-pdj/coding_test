def sol1(money, costs):
    # 비율 
    coins = [1, 5, 10, 50, 100, 500]
    rate = []
    for i in range(6):
        rate.append((costs[i] / coins[i] , i))
    rate.sort()

    # 그리디
    answer = 0
    for a, b in rate:
        answer += (money // coins[b]) * costs[b]
        money = money % coins[b]
    
    return answer
  
  
def sol2(n, clockwise):
    answer = [[0] * n for _ in range(n)]

    # 배열 구성
    count = 1
    for i in range(n // 2):
        for j in range((n - 1) - (i * 2)):
            # 4방향에서 해당 값을 삽입
            answer[i][j + i] = count
            answer[n - 1 - i][n - 1 - j - i] = count
            answer[j + i][n - 1 - i] = count
            answer[n - 1 - j - i][i] = count
            count += 1

    # 홀수 인 경우 가운데 체크
    if n % 2 == 1:
        answer[n // 2][n // 2] = count

    # False인 경우
    if not clockwise:
        answer = answer[::-1]

    return answer
  
  
def sol3(width, height, diagonals):
    # 세는 용도의 배열
    count = [[1] * (width + 1) for _ in range(height + 1)]
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            count[i][j] = (count[i - 1][j] + count[i][j - 1]) % 10000019

    # 대각선을 꼭 한번 지나가야하므로
    # 대각선 양점을 기준으로 가능 갯수 계산 
    answer = 0
    for y, x in diagonals:
        # (0, 0) -> (x - 1, y) -> (x, y - 1) -> (height, width)
        answer += (count[x - 1][y] * count[height - x][width - y + 1]) % 10000019

        # (0, 0) -> (x, y - 1) -> (x - 1, y) -> (height, width)
        answer += (count[x][y - 1] * count[height - x + 1][width - y]) % 10000019

    return answer % 10000019
  
  
#from itertools import combinations
#from collections import defaultdict, deque
# 최적화 실패

def sol4(n, edges):
    global check, dic

    # 그래프 구성
    dic = defaultdict(list)
    for a, b in edges:
        dic[a].append(b)
        dic[b].append(a)

    # 연산량 개선을 위한 저장용 배열
    check = [[-1] * n for _ in range(n)]

    # 3개를 선택하여 체크
    count = 0
    for i, j, k in combinations(range(0, n), 3):
        a, b, c = dist(i, j), dist(j, k), dist(i, k)
        if a + b == c or a + c == b or b + c == a:
            count += 1

    return count * 2
  
# 간선 거리 계산 함수
def dist(a, b):
    global check, dic

    # 이미 구했던 경우 
    if check[a][b] != -1:
        return check[a][b]
    else:
        # bfs 탐색
        queue = deque([(a, 0, -1)])

        while queue:
            now, depth, before = queue.popleft()

            # 탐색 완료시 저장 후 반환
            if now == b:
                check[a][b] = depth
                return depth
            
            for i in dic[now]:
                if i != before:
                    queue.append((i, depth + 1, now))
