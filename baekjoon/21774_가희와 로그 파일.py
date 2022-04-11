import sys, re, bisect
input = sys.stdin.readline
    
# 파싱
n, q = map(int, input().split())
log = [[] for _ in range(7)]
for _ in range(n):
    temp = input().rstrip().split("#")
    temp[0] = int(re.sub("[^0-9]", "", temp[0]))
    temp[1] = int(temp[1])
    
    for i in range(1, temp[1] + 1):
        log[i].append(temp[0])

# 쿼리 처리
for _ in range(q):
    temp = input().rstrip().split("#")
    temp[0] = int(re.sub("[^0-9]", "", temp[0]))
    temp[1] = int(re.sub("[^0-9]", "", temp[1]))
    temp[2] = int(temp[2])
    
    # 해당 레밸에 맞는 춰리에서 이분탐색
    start = bisect.bisect_left(log[temp[2]], temp[0])
    end = bisect.bisect_right(log[temp[2]], temp[1])
    
    # 결과 출력
    print(end - start)
