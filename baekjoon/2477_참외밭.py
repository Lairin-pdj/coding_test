import sys
input = sys.stdin.readline

# 파싱
k = int(input())
n = [list(map(int, input().split())) for _ in range(6)]

# 계산
for i in range(9):
    # 치환
    a, b, c, d = (i) % 6, (i + 1) % 6, (i + 2) % 6, (i + 3) % 6
    
    # 반복 부분 체크
    if n[a][0] == n[c][0] and n[b][0] == n[d][0]:
        
        # 결과출력
        print((((n[a][1] + n[c][1]) * (n[b][1] + n[d][1])) - (n[b][1] * n[c][1])) * k)
        
        break
