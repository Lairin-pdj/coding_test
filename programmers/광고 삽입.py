def htos(time):
    # 주어진 시간을 초로 변환
    temp = list(map(int, time.split(":")))
    
    return temp[0] * 3600 + temp[1] * 60 + temp[2]

def stoh(time):
    # 주어진 초를 시간으로 변환
    hour = str(time // 3600)
    minute = str((time // 60) % 60)
    second = str(time % 60)
    
    return hour.zfill(2) + ":" + minute.zfill(2) + ":" + second.zfill(2)

def solution(play_time, adv_time, logs):
    # 영상시간과 광고시간이 같을 경우
    if play_time == adv_time:
        return "00:00:00"

    # 시간들 변환하여 저장
    playtime = htos(play_time)
    advtime = htos(adv_time)
    
    # 시간 저장용 배열 생성
    watcher = [0 for _ in range(playtime + 1)]
    
    # 로그를 분석하여 시작시간과 끝시간 체크
    for i in logs:
        a, b = i.split("-")
        watcher[htos(a)] += 1
        watcher[htos(b)] += -1

    # 시간별 시청자 수의 합 배열로 변환
    for i in range(1, playtime + 1):
        watcher[i] += watcher[i - 1]

    # 누적 시청시간 배열로 변환
    for i in range(1, playtime + 1):
        watcher[i] += watcher[i - 1]
    
    # 시청시간으로 최댓값 도출
    answer = 0
    temp = watcher[advtime - 1]
    for i in range(playtime - advtime):
        if temp < watcher[i + advtime] - watcher[i]:
            temp = watcher[i + advtime] - watcher[i]
            answer = i + 1
            
    return stoh(answer)
