def solution(dirs):
    # 집합을 통해 중복 제거 = 되돌아가는길 카운트 x
    route = set()
    now = [0, 0]
    
    for i in dirs:
        # 각 지시에 맞게 움직이나 좌표 밖으로 이동이면 차단
        if i == "U" and now[1] + 1 <= 5:
            # 되돌아가는 것도 체크하기 위해 정렬
            temp = [now, [now[0], now[1] + 1]]
            temp.sort()
            route.add(tuple(temp[0] + temp[1]))
            now = [now[0], now[1] + 1]
        elif i == "D" and now[1] - 1 >= -5:
            temp = [now, [now[0], now[1] - 1]]
            temp.sort()
            route.add(tuple(temp[0] + temp[1]))
            now = [now[0], now[1] - 1]
        elif i == "L" and now[0] - 1 >= -5:
            temp = [now, [now[0] - 1, now[1]]]
            temp.sort()
            route.add(tuple(temp[0] + temp[1]))
            now = [now[0] - 1, now[1]]
        elif i == "R" and now[0] + 1 <= 5:
            temp = [now, [now[0] + 1, now[1]]]
            temp.sort()
            route.add(tuple(temp[0] + temp[1]))
            now = [now[0] + 1, now[1]]
    
    return len(route)
