import re

# 시간을 숫자로 변환해주는 함수
def time2int(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)

def solution(m, musicinfos):
    # 가능한 곡들을 담는 리스트
    temp = []
    
    # 노래마다 체크
    for num, music in enumerate(musicinfos):
        start, end, name, song = music.split(",")
        start = time2int(start)
        end = time2int(end)
        # 노래의 실행시간을 기록
        time = end - start
        
        # 실행시간동안 실제로 재생된 음 목록 생성
        real = ""
        i = 0
        while i < time:
            real += song[i % len(song)]
            i += 1
            # #의 경우에는 추가적인 체크
            if song[i % len(song)] == "#":
                real += song[i % len(song)]
                i += 1
                time += 1
        
        # 재생된 음에서 들은 부분이 존재하는지 전부 체크
        for check in re.finditer(m, real):
            idx = check.start()
            # 문구가 끝난 뒤 #이 있을 경우는 문제가 있는 경우이기에 제외
            if not (idx + len(m) < len(real) and real[idx + len(m)] == "#"):
                temp.append([end - start, name, num])
                break
    
    # 노래가 여러 곡일 경우 조건에 맞게 정렬
    if len(temp) > 0:
        temp.sort(key = lambda x : (-x[0], x[2]))
        return temp[0][1]
    # 노래가 없는 경우
    else:
        return "(None)"
