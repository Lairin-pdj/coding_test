from itertools import combinations
import sys
input = sys.stdin.readline

# 파싱
n = int(input())

# 1022번째가 9876543210으로 1023번째 부턴 불가능
if n >= 1023:
    print(-1)

# 숫자조합을 이용해 모든 수 체킹
else:
    answers = []
    
    for i in range(1, 11):
        for j in combinations(range(9, -1, -1), i):
            answers.append(int("".join(map(str, j))))
    
    answers.sort()
    print(answers[n])
