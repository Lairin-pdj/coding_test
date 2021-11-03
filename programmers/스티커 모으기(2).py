def solution(sticker):
    # 1장만 있을 경우 바로 반환
    if len(sticker) == 1:
        return sticker[0]
    
    # 0번째 스티커가 선택되는 경우와 1번째 스티커가 선택되는 경우를 나누기 위해 dp1과 dp2로 분리
    # 직전의 스티커를 선택한 경우와 지금 스티커를 선택하는 경우의 최댓값 비교
    dp1 = [0 for _ in range(len(sticker))]
    dp1[0] = sticker[0]
    if sticker[0] > sticker[1]:
        dp1[1] = sticker[0]
        for i in range(2, len(sticker) - 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])
    else:
        dp1[1] = sticker[1]
        for i in range(2, len(sticker)):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])
        
    dp2 = [0 for _ in range(len(sticker))]
    dp2[1] = sticker[1]
    
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    return max(dp1[-2], dp2[-1])
