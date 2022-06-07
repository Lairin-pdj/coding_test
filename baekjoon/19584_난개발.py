from collections import defaultdict
import sys
input = sys.stdin.readline
    
# 파싱
n, m = map(int, input().split())
dic = defaultdict(int)
for i in range(1, n + 1):
    dic[i] = int(input().split()[1])

# 도로 시작 끝 체크
start, end = [], []
for _ in range(m):
    u, v, c = map(int, input().split())
    a, b = dic[u], dic[v]
    if a > b:
        a, b = b, a
    
    start.append((a, c))
    end.append((b, c))

# 스위핑을 위한 정렬
start.sort()
end.sort()

# 투 포인터
i, j = 0, 0
answer = 0
now = 0
while i < m:
    
    if start[i][0] <= end[j][0]:
        now += start[i][1]
        answer = max(answer, now)
        i += 1
    else:
        now -= end[j][1]
        j += 1

# 결과 출력
print(answer)
