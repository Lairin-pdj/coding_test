from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())

# 점수판 체크
scores = []
for _ in range(n):
    scores.append(list(map(int, input().split(" "))))

# 집합을 활용
mans = [i for i in range(n)]
check = set(mans)

low = 1000000000
# 팀을 나누는 모든 경우의 수 체크
for a in combinations(mans, n // 2):
    # 팀 집합 생성
    team1 = set(a)
    team2 = check - team1
    
    # 팀1의 점수 계산
    team1_score = 0
    for b in combinations(team1, 2):
        team1_score += scores[b[0]][b[1]] + scores[b[1]][b[0]]
    
    # 팀2의 점수 계산
    team2_score = 0
    for b in combinations(team2, 2):
        team2_score += scores[b[0]][b[1]] + scores[b[1]][b[0]]

    # 차이값 체크
    low = min(low, abs(team1_score - team2_score))
    
print(low)
