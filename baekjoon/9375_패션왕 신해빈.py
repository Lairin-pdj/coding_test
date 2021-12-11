from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
t = int(input())
for _ in range(t):
    n = int(input())
    # 종류 체크
    dic = defaultdict(int)
    for _ in range(n):
        a, b = input().rstrip().split()
        dic[b] += 1
    
    # 경우의 수 계산 및 결과 출력
    count = 1
    for i in dic.values():
        count *= (i + 1)
    print(count - 1)
