from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
dic = defaultdict(int)
# 해싱
for _ in range(n):
    name = input().rstrip()
    dic[name] = 1

# 겹치기
result = []
for _ in range(m):
    name = input().rstrip()
    if dic[name] == 1:
        result.append(name)
result.sort()

# 결과 출력
print(len(result))
for name in result:
    print(name)
