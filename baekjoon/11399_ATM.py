import sys
input = sys.stdin.readline

# 파싱
n = int(input())
times = list(map(int, input().split()))

# 정렬
times.sort()

# 누적합
count = 0
total = 0
for i in times:
    count += i
    total += count
    
# 결과 출력
print(total)
