import sys
input = sys.stdin.readline

# 파싱
n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

# dp
answer = 1000001
# 시작점을 기준으로 반복 체크
for j in range(3):
    # 최댓값을 조정하여 강제 선택 유도
    if j == 0:
        temp = [[costs[0][0], 1001, 1001]]
    elif j == 1:
        temp = [[1001, costs[0][1], 1001]]
    else:
        temp = [[1001, 1001, costs[0][2]]]
    for i in range(1, n):
        temp.append([costs[i][0], costs[i][1], costs[i][2]])
    
    # dp 진행
    for i in range(1, n):
        temp[i][0] += min(temp[i - 1][1], temp[i - 1][2])
        temp[i][1] += min(temp[i - 1][0], temp[i - 1][2])
        temp[i][2] += min(temp[i - 1][0], temp[i - 1][1])
    
    # 첫번째 선택과 어긋나지 않도록 최솟값 체크
    if j == 0:
        answer = min(answer, min(temp[n - 1][1], temp[n - 1][2]))
    elif j == 1:
        answer = min(answer, min(temp[n - 1][0], temp[n - 1][2]))
    else:
        answer = min(answer, min(temp[n - 1][0], temp[n - 1][1]))

# 결과 출력
print(answer)
