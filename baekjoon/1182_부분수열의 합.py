import sys 
input = sys.stdin.readline
sys.setrecursionlimit(3000000)

def back(many, idx, total):
    global count
    # 정답일 경우
    if many != 0 and total == s:
        count += 1
    
    # 탈출
    if idx >= n:
        return
    
    # 삽입
    for i in range(idx, n):
        back(many + 1, i + 1, total + nums[i])

# 파싱
n, s = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

# 재귀
count = 0
back(0, 0, 0)

# 결과 출력
print(count)
