from collections import defaultdict
import sys
input = sys.stdin.readline
    
# 파싱
n = int(input())
child = defaultdict(list)
check = set()
for _ in range(n):
    p, l, r = map(int, input().split())
    child[p] = [l, r]
    check.add(l)
    check.add(r)

# 루트 찾기
root = 0
for i in range(1, n + 1):
    if i not in check:
        root = i
        break

# 순회
count = 1
diff = defaultdict(list)
def dfs(now, depth):
    global count
    left = child[now][0] 
    right = child[now][1]
    
    if left != -1:
        dfs(left, depth + 1)
    diff[depth].append(count)
    count += 1
    if right != -1:
        dfs(right, depth + 1)

# 실행
dfs(root, 1)

# 최댓값 체크
answer = 0 
level = 0
temp = list(diff.keys())
temp.sort()
for i in temp:
    width = max(diff[i]) - min(diff[i]) + 1
    if width > answer:
        answer = width
        level = i

# 결과출력
print(level, answer)
