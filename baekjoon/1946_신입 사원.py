import sys
input = sys.stdin.readline

# 케이스 수
t = int(input())

# 케이스 별 진행
for _ in range(t):
    # 파싱
    n = int(input())
    ranks = []
    for i in range(n):
        a, b = list(map(int, input().split()))
        ranks.append((a, b))
    
    # 정렬
    ranks.sort()
    
    # 순위가 높아지는 것만 기록
    count = 0
    temp = ranks[0][1]
    for a, b in ranks:
        if b <= temp:
            count += 1
            temp = b
    
    # 결과 출력
    print(count)
