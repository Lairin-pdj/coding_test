import sys
input = sys.stdin.readline

# 파싱
n, s = map(int, input().split())
nums = list(map(int, input().split()))

# 합이 처음으로 s를 넘는 경우 탐색
i, j = 0, 0
count = nums[0]
while count < s and j + 1 < n:
    j += 1
    count += nums[j]
    
# 전부 합쳐도 안되는 경우
if count < s:
    print(0)
else:
    answer = j - i + 1
    
    # 값을 체크하며 i, j 전진
    while i <= j and j < n:
        if count >= s:
            answer = min(answer, j - i + 1)
            count -= nums[i]
            i += 1
        else:
            if j + 1 >= n:
                break
            j += 1
            count += nums[j]
    
    # 결과 출력
    print(answer)
