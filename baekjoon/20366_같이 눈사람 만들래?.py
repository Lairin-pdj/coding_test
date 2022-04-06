import sys
input = sys.stdin.readline
    
# 파싱
n = int(input())
nums = list(map(int, input().split()))

# 조합
comb = []
for i in range(n - 1):
    for j in range(i + 1, n):
        comb.append((nums[i] + nums[j], i, j))
comb.sort()

# 순회
answer = 1000000000
for i in range(len(comb) - 1):

    temp = set([comb[i][1], comb[i][2], comb[i + 1][1], comb[i + 1][2]])
    if len(temp) == 4:
        answer = min(answer, comb[i + 1][0] - comb[i][0])

# 결과 출력
print(answer)
