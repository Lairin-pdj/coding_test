import sys
input = sys.stdin.readline
    
# 파싱
n = int(input())
nums = [input().rstrip() for _ in range(n)]
length = len(nums[0])

# 자리수를 늘려가며 체크
answer = 0
for i in range(1, length + 1):
    flag = True
    
    check = set()
    
    for num in nums:
        temp = num[-i:]
        if temp not in check:
            check.add(temp)
        else:
            flag = False
            break
    
    if flag:
        answer = i
        break

# 결과 출력
print(answer)
