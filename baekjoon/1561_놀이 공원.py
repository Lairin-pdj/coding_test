import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
plays = list(map(int, input().split()))

# 이분탐색
low = 0
high = ((n // m) + 1) * 30
while low <= high:
    mid = (low + high) // 2
    
    # 계산
    count = 0
    for i in plays:
        count += (mid // i) + 1
    
    # 이동
    if count < n:
        low = mid + 1
    else:
        high = mid - 1

# 현재 명수 
count = 0
target = []
for i in range(len(plays)):
    if low % plays[i] == 0:
        target.append(i + 1)
    count += (low // plays[i]) + 1

# 결과 출력
print(target[len(target) - (count - n + 1)])
