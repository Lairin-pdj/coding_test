import sys
input = sys.stdin.readline

# 입력 파싱
n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split(" "))))
    
# 모든 수 순회
for i in range(1, n):
    for j in range(i + 1):
        # 좌우 값 중 큰 것으로 합체
        if j == 0:
            lines[i][j] += lines[i - 1][j]
        elif j == i:
            lines[i][j] += lines[i - 1][j - 1]
        else:
            lines[i][j] += max(lines[i - 1][j], lines[i - 1][j - 1])

# 최댓값 출력
print(max(lines[-1]))
