import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))

# 누적합
for i in range(1, n):
    nums[i] += nums[i - 1]
    
# 4로 나누어 떨어지지 않는 경우
if nums[-1] % 4 != 0:
    print(0)
# 가능한 경우
else:
    # 가능한 분기점에서 체크
    temp = nums[-1] // 4
    n1, n2, n3 = temp, temp * 2, temp * 3
    c0, c1, c2, c3 = 1, 0, 0, 0
    for i in range(n - 1):
        if nums[i] == n3:
            c3 += c2
        if nums[i] == n2:
            c2 += c1
        if nums[i] == n1:
            c1 += c0
    
    # 결과 출력
    print(c3)
