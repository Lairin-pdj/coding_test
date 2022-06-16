import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
check = set()
for _ in range(n):
    check.add(input().rstrip())

# 체크
count = 0
for _ in range(m):
    if input().rstrip() in check:
        count += 1

# 결과 출력
print(count)
