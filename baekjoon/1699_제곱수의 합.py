import sys
input = sys.stdin.readline

# 파싱
n = int(input())

# dp
dp = [i for i in range(n + 1)]

for i in range(1, n + 1):
    j = 1
    
    while j * j <= i:
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1
        
        j += 1
    
# 결과 출력
print(dp[n])


'''
# 조금 느림
import sys
input = sys.stdin.readline

# 파싱
n = int(input())

# dp
dp = [100000 for _ in range(n + 1)]
for i in range(1, int(n ** 0.5) + 1):
    dp[i * i] = 1

for i in range(1, n + 1):
    for j in range(1, int(n ** 0.5) + 1):
        if i + j * j > n:
            break
        else:
            dp[i + j * j] = min(dp[i] + 1, dp[i + j * j])

# 결과 출력
print(dp[n])
'''
