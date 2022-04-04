from collections import defaultdict
import sys
input = sys.stdin.readline
    
# 파싱
size = int(input())
m, n = map(int, input().split())
left = [int(input()) for _ in range(m)]
right = [int(input()) for _ in range(n)]

# 누적합 
for i in range(1, len(left)):
    left[i] += left[i - 1]
for i in range(1, len(right)):
    right[i] += right[i - 1]
lall, rall = left[-1], right[-1]
left = [0] + left[:-1]
right = [0] + right[:-1]

# 가능한 조합 계산
ldic = defaultdict(int)
for i in range(len(left)):
    for j in range(len(left)):
        if i != j:
            ldic[((left[i] - left[j]) % lall)] += 1
ldic[lall] += 1
rdic = defaultdict(int)
for i in range(len(right)):
    for j in range(len(right)):
        if i != j:
            rdic[((right[i] - right[j]) % rall)] += 1
rdic[rall] += 1

# 결과 계산
answer = 0
for key in ldic.keys():
    if key < size:
        if (size - key) in rdic:
            answer += rdic[size - key] * ldic[key]
    elif key == size:
        answer += ldic[key]

if size in rdic:
    answer += rdic[size]

# 결과 출력
print(answer)
