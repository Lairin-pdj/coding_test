import sys, math
input = sys.stdin.readline

# 파싱
n, atk = map(int, input().split())
damagetop = 0
nowtop, nowlow = 0, 0
now = 0
for _ in range(n):
    t, a, h = map(int, input().split())
    
    # 몬스터일 경우
    if t == 1:
        temp = int(math.ceil(h / atk) - 1) * a
        now += temp
        damagetop = max(damagetop, temp)
        
        # 특수 케이스 처리
        # now의 nowtop 갱신시 
        if now >= nowtop:
            # 초과 회복이 되지 않았던 경우
            if nowlow == 0: 
                nowtop = now
            # 초과 회복을 하고 갱신이 되는 경우
            else:
                nowtop -= nowlow
                now -= nowlow
                nowlow = 0

    # 물약일 경우
    else:
        atk += a
        now -= h
        nowlow = min(nowlow, now)
    
# 결과 출력
print(damagetop + 1 if nowtop < damagetop else nowtop + 1)
