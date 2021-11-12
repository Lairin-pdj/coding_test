import sys
input = sys.stdin.readline

# 파싱
n = int(input())
point = [list(map(int, input().split())) for _ in range(n)]

# 다각형의 넓이 계산
# 가우스의 면적공식
point.append(point[0])
left, right = 0, 0
for i in range(1, n + 1):
    left += point[i - 1][0] * point[i][1]
    right += point[i - 1][1] * point[i][0]
    
# 결과 출력
print(round(abs(left - right) / 2, 1))
