import sys
input = sys.stdin.readline

# 파싱
a, b, d, n = map(int, input().split())

# dp[i] => i번째 날 태어난 개체 수
dp = [0 for _ in range(n + 1)]
dp[0], total, adult = 1, 1, 0

# 당일 성장일 경우 예외
if a == 1:
    adult = 1

# dp 진행
for i in range(1, n + 1):
    # 성체 수 만큼 태어남
    dp[i] = adult
    
    # 전날에서 태어난 수 더하고, 죽은 수 제거
    total += adult
    if i - d >= 0:
        total -= dp[i - d]
    total %= 1000
    
    # 전날에서 성장한 숫자 더하고, 늙은 수 제거
    if i - a + 1 >= 0:
        adult += dp[i - a + 1]
    if i - b + 1 >= 0:
        adult -= dp[i - b + 1]
    adult %= 1000

# 결과 출력
print(total % 1000)
