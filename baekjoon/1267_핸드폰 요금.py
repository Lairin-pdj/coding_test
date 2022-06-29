import sys
input = sys.stdin.readline

# 파싱
n = int(input())
times = list(map(int, input().split()))

# 계산
y, m = 0, 0
for i in times:
    y += ((i // 30) + 1) * 10
    m += ((i // 60) + 1) * 15

# 결과 출력
if y > m:
    print("M", m)
elif m > y:
    print("Y", y)
else:
    print("Y M", y)
