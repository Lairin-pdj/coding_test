import sys
input = sys.stdin.readline

# 파싱
n = int(input())
rin, rout = [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    rin.append(b / c)
    rout.append(d / a)

# 정렬
rin.sort()
rout.sort()

# 교차 체크
answer, temp = 0, 0
i, j = 0, 0
while i < n:
    
    # 들어가기
    if rin[i] <= rout[j]:
        i += 1
        temp += 1
        answer = max(answer, temp)
    # 나가기
    elif rin[i] > rout[j]:
        j += 1
        temp -= 1

# 결과 출력
print(answer)
