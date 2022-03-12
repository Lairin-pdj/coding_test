from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 파싱
nums = ""
for _ in range(3):
    nums += input().rstrip().replace(" ", "")
    
empty = -1
for i in range(len(nums)):
    if nums[i] == "0":
        empty = i
        break

# bfs
answer = -1
check = defaultdict(bool)
queue = deque([(nums, empty, 0)])
check[nums] = True
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1] 
while queue:
    now, hole, count = queue.popleft()
    x, y = hole // 3, hole % 3
    
    # 탈출 조건
    if now == "123456780":
        answer = count
        break
    
    # 가능한 방향으로 이동
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        new = ax * 3 + ay
        
        if 0 <= ax < 3 and 0 <= ay < 3:
            # 해당 숫자를 이동
            temp = int(now) - int(now[new]) * (10 ** (8 - new)) + (int(now[new]) * (10 ** (8 - hole)))
            temp = str(temp).zfill(9)
            if temp not in check:
                queue.append((temp, new, count + 1))
                check[temp] = True

# 결과 출력
print(answer)
