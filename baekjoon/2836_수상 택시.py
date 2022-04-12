import sys
input = sys.stdin.readline
    
# 파싱
n, m = map(int, input().split())
nums = []
for _ in range(n):
    a, b = map(int, input().split())
    
    # 돌아가야하는 경우만 체크
    if a > b:
        nums.append((b, a))

# 순서대로 체크하기 위한 정렬
nums.sort()

# 돌아가야하는 길이 체크
back = 0
if nums:
    start, end = nums[0][0], nums[0][1]
    
    # 연결되는 부분을 한번에 처리
    for a, b in nums:
        if end > a:
            end = max(end, b)
        else:
            back += end - start
            start = a
            end = b
    
    # 남은 거리 처리
    back += end - start

# 결과 출력
print(m + 2 * back)
