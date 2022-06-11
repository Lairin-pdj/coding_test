import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

# 재귀
def rec(a, b, c, prev):

    # 적합할 경우 결과 출력
    if (a, b, c) == (ta, tb, tc):
        print("".join(answer))
        exit(0)
    
    # 최적화
    if dp[a][b][c][prev[0]][prev[1]]:
        return False

    dp[a][b][c][prev[0]][prev[1]] = True
    
    # a, b, c 중 하나 선택
    if ta >= a + 1:
        answer[a + b + c] = "A"
        rec(a + 1, b, c, [prev[1], 0])
    if tb >= b + 1:
        if prev[1] != 1:
            answer[a + b + c] = "B"
            rec(a, b + 1, c, [prev[1], 1])    
    if tc >= c + 1:
        if prev[0] != 2 and prev[1] != 2:
            answer[a + b + c] = "C"
            rec(a, b, c + 1, [prev[1], 2])
    
# 파싱
record = input().rstrip()

# 갯수 체크
ta, tb, tc = 0, 0, 0
for i in record:
    if i == "A":
        ta += 1
    elif i == "B":
        tb += 1
    else:
        tc += 1

# 결과 계산
length = len(record)
answer = [""] * length
dp = [[[[[False] * 3 for _ in range(3)] for _ in range(length)] for _ in range(length)] for _ in range(length)]
rec(0, 0, 0, [0, 0])

# 찾지 못한 경우
print(-1)
