def solution(name):
    answer = 0
    a = ord('A')
    now = []
    for i, x in enumerate(name):                # 각 문자들을 A로 바꾸기 위한 비용 합산
        if x != "A":
            now.append(i)
            temp = ord(name[i]) - a
            answer += min(temp, 26 - temp)
            
    if now[0] == 0:                             # 현재 위치 제거
        now.pop(0)
        
    nowleft = now[::-1]                         # 좌측과 우측 이동을 나눠 계산하기 위해
    leftfirst = 0
    rightfirst = 0
    
    cursor = 0
    while len(now) > 0:                         # 전부 사용할 때까지 현재 좌표에서 이동거리 짧은 것 계산하며 이동
        temp = []
        for i in now:
            temp.append(min(abs(i - cursor), len(name) - i + cursor))
        rightfirst += min(temp)
        cursor = now[temp.index(min(temp))]
        now.pop(temp.index(min(temp)))
        
    cursor = 0
    while len(nowleft) > 0:                     # 좌측도 마찬가지로 진행
        temp = []
        for i in nowleft:
            temp.append(min(abs(i - cursor), abs(len(name) - abs(i - cursor))))
        leftfirst += min(temp)
        cursor = nowleft[temp.index(min(temp))]
        nowleft.pop(temp.index(min(temp)))
        
    return answer + min(rightfirst, leftfirst)  # 최솟값 반환
