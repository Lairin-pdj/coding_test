import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input().rstrip()[-3:]))

# 가능한 사람 수 1 ~ 1000
for i in range(1, 1001):
    
    # 모든 경우에 대해 체크
    flag = True
    for num in nums:
        low = num * i
        high = (num + 1) * i
        
        # 바로 나눠 떨어지는 경우
        if low % 1000 != 0:
            # 소수점이 잘리며 발생하는 오차 해결
            if (low // 1000) == ((high - 1) // 1000): 
                flag = False
                break
    
    # 모든 경우가 만족할 경우 출력
    if flag:
        print(i)
        break
