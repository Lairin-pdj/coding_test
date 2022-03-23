import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 나머지
remain = [0 for _ in range(m)]
nums[0] %= m
remain[nums[0]] += 1

# 누적합 및 나머지 처리
for i in range(1, n):
    nums[i] = (nums[i] + nums[i - 1]) % m
    remain[nums[i]] += 1

# nCr 갯수 반환 함수
def com(n, r):
    if r < 0 or n < r:
        return 0
    temp = 1
    for i in range(n, n - r, -1):
        temp *= i
    for i in range(1, r + 1):
        temp = temp // i
    return temp

# 갯수 체크
count = remain[0]
for i in range(m):
    count += com(remain[i], 2)

# 결과 출력
print(count)
