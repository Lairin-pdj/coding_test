import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
gems = [0]
for _ in range(n):
    gems.append(int(input()))

# 누적합
for i in range(1, n):
    gems[i + 1] += gems[i]

# 부분 최대합 구간 체크
sub = 0
high = 0
for i in range(m - 1, n):
    sub = min(sub, gems[i - (m - 1)])
    high = max(high, gems[i + 1] - sub)

# 결과 출력
print(high)
