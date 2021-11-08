import sys
input = sys.stdin.readline

# 파싱
n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]

# 정렬
times.sort(key = lambda x : (x[1], x[0]))

# 그리드
# 회의가 끝나는 시간을 기록
end = 0
count = 0
for s, e in times:
    if s >= end:
        end = e
        count += 1

# 결과 출력
print(count)
