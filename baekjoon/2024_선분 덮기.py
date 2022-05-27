from collections import deque
import sys
input = sys.stdin.readline

# 파싱
m = int(input())
lines = []
while True:
    l, r = map(int, input().split())
    
    if l == 0 and r == 0:
        break
    
    if l == r:
        continue
    
    if l < 0 and r <= 0:
        continue
    
    lines.append((l, r))

# 정렬
lines = deque(sorted(lines))

# 스위핑
def counter(line):
    checked = 0
    count = 0
    
    while line:
        can = []
        l, r = line.popleft()
        if l <= checked:
            can.append(r)
        else:
            return 0
        
        while line:
            if line[0][0] <= checked:
                can.append(line[0][1])
                line.popleft()
            else:
                break
        
        checked = max(can)
        count += 1
        
        if checked >= m:
            return count
    
    return 0

# 결과 출력
print(counter(lines))
