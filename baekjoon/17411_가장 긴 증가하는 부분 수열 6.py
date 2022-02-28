from collections import defaultdict
import sys, bisect
input = sys.stdin.readline

# 파싱
n = int(input())
lines = list(map(int, input().split()))
dic = defaultdict(list)

# 이분탐색을 이용한 nlogn LIS
lis = []
index = [-1 for _ in range(n)]
for i, x in enumerate(lines):
    idx = bisect.bisect_left(lis, x)
    if idx >= len(lis):
        lis.append(x)
    else:
        lis[idx] = x
    index[i] = idx

# 갯수 체크
dp = [[0] for _ in range(len(lis))]
for i in range(n - 1, -1, -1):
    target = 1
    if index[i] + 1 < len(lis):
        temp = bisect.bisect_right(dic[index[i] + 1], lines[i])
        target = dp[index[i] + 1][-1] - dp[index[i] + 1][temp]
    dic[index[i]].append(lines[i])
    dp[index[i]].append((target + dp[index[i]][-1]) % 1000000007)

# 결과 출력
print(len(lis), end = " ")
print(dp[0][-1])
