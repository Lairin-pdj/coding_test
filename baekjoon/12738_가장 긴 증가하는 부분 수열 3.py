import sys, bisect
input = sys.stdin.readline

# 파싱
n = int(input())
lines = list(map(int, input().split()))

# 이분탐색을 이용한 nlogn LIS
lis = []
for i in lines:
    idx = bisect.bisect_left(lis, i)
    if idx >= len(lis):
        lis.append(i)
    else:
        lis[idx] = i

# 결과 출력
print(len(lis))
