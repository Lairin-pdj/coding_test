import sys
input = sys.stdin.readline

# 파싱
n, k = map(int, input().split())
feed = list(map(int, input().split()))

# 부분합이 k를 넘는 먹이뭉치 탐색
answer = [0] * (n + 1)
now, left = 0, 0
for right in range(n):
    
    # 기존 값이 더 큰 경우 체크
    answer[right + 1] = max(answer[right + 1], answer[right])
    
    # 먹이를 하나씩 추가
    now += feed[right]
    
    # k를 넘는 먹이뭉치 dp
    while now >= k:
        answer[right + 1] = max(answer[right + 1], answer[left] + (now - k))
        now -= feed[left]
        left += 1

# 결과 출력
print(answer[n])
