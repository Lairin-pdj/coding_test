import sys
input = sys.stdin.readline

# 파싱
s, a, b, c = map(int, input().split())

# nCr
def comb(n, r):
    if r < 0 or n < r:
        return 0
        
    temp = 1
    for i in range(n, n - r, -1):
        temp *= i
    for i in range(1, r + 1):
        # float 오버플로를 막기 위해 
        temp = temp // i
    return temp

# 불가능한 경우
if s > a + b + c:
    print(0)
# 가능한 경우
else:

    # 자유롭게 선택하는 경우의 수
    answer = (comb(s, a) * comb(s, b) * comb(s, c)) % 1000000007
    
    # 선택되지 않은 곡이 있는 경우의 수
    for i in range(1, s - max(a, b, c) + 1):
        temp = (comb((s - i), a) * comb((s - i), b) * comb((s - i), c) * comb(s, i)) % 1000000007
        answer += ((-1) ** i) * temp
        answer = answer % 1000000007

    # 결과 출력
    print(answer)
    
'''
# 재귀를 이용한 dp 풀이
import sys
input = sys.stdin.readline
sys.setrecursionlimit(6250000)

# 파싱
s, a, b, c = map(int, input().split())

# dp
def rec(s, a, b, c):
    
    # 시작값
    if s == 0:
        if a == 0 and b == 0 and c == 0:
            return 1
        else:
            return 0
    
    # 접근 불가 값 제거
    if a < 0 or b < 0 or c < 0:
        return 0
    
    # 중복 체크 제거
    if dp[s][a][b][c] != -1:
        return dp[s][a][b][c]
    
    # 값 계산
    temp = rec(s - 1, a - 1, b - 1, c - 1)
    temp += rec(s - 1, a, b - 1, c - 1)
    temp += rec(s - 1, a - 1, b, c - 1)
    temp += rec(s - 1, a - 1, b - 1, c)
    temp += rec(s - 1, a, b, c - 1)
    temp += rec(s - 1, a, b - 1, c)
    temp += rec(s - 1, a - 1, b, c)
    
    temp = temp % 1000000007
    
    # 결과 반영 및 반환
    dp[s][a][b][c] = temp
    return temp

    
dp = [[[[-1] * (c + 1) for _ in range(b + 1)] for _ in range(a + 1)] for _ in range(s + 1)]

# 결과 출력
print(rec(s, a, b, c))
'''
