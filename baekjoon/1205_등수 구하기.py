from bisect import bisect_right
import sys
input = sys.stdin.readline

# 파싱
n, score, p = map(int, input().split())
if n == 0:
    print(1)
else:
    scores = list(map(int, input().split()))
    scores.sort()
    
    if n == p and scores[0] >= score:
        print(-1)
    else:
        idx = (n - bisect_right(scores, score)) + 1
        print(idx)
