import sys
input = sys.stdin.readline

# 파싱
n = int(input())
buildings = list(map(int, input().split()))

# 빌딩마다 전부 계산
bcount = [0 for _ in range(n)]

# 자신의 오른쪽 편에 볼 수 있는 빌딩 체크
for i in range(n - 1):
    incli = -1000000000
    for j in range(i + 1, n):
        now = (buildings[j] - buildings[i]) / (j - i)
        if now > incli:
            incli = now
            bcount[i] += 1

# 자신의 왼쪽 편에 볼 수 있는 빌딩 체크
for i in range(n - 1, 0, -1):
    incli = -1000000000
    for j in range(i - 1, -1, -1):
        now = (buildings[i] - buildings[j]) / (j - i)
        if now > incli:
            incli = now
            bcount[i] += 1

# 최댓값 출력
print(max(bcount))
