import sys
input = sys.stdin.readline
    
# 파싱
n = int(input())
paper = [[0] * 101 for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    # 종이 기록 (n^2)
    for i in range(10):
        for j in range(10):
            paper[x + i][y + j] = 1

# 연속 부분 체크 (n^2)
for i in range(101):
    for j in range(1, 101):
        if paper[i][j] == 1:
            paper[i][j] += paper[i][j - 1]

# 모든 지점에서의 가능성 체크 (n^3)
answer = 0
for i in range(101):
    for j in range(1, 101):
        temp = paper[i][j]
        if temp != 0:
            for k in range(i + 1, 101):
                temp = min(temp, paper[k][j])
                answer = max(answer, temp * (k - i + 1))
                
                if temp == 0:
                    break

# 결과 출력
print(answer)
