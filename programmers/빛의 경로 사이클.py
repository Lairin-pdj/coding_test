from collections import Counter

def solution(grid):
    hang = len(grid)
    yeol = len(grid[0])
    
    # 빛의 이동 정보 배열 초기화
    light = []
    for i in range(hang):
        temp = []
        for j in range(yeol):
            temp.append([-1, -1, -1, -1])
        light.append(temp)
    
    # 모든 방향에 대한 데이터 체크
    check = 1
    for i in range(hang):
        for j in range(yeol):
            for k in range(4):
                # 진행 된 기록이 없다면 
                if light[i][j][k] == -1:
                    # 빛이 들어온 것으로 판단하고 진행
                    tempi = i
                    tempj = j
                    tempk = k
                    light[tempi][tempj][tempk] = check
                    while True:
                        # 회전의 경우
                        if grid[tempi][tempj] == "L":
                            tempk = (tempk - 1) % 4
                        elif grid[tempi][tempj] == "R":
                            tempk = (tempk + 1) % 4
                        
                        # 이동
                        if tempk % 2 == 0:
                            tempi = (tempi + (tempk - 1)) % hang
                        else:
                            tempj = (tempj - (tempk - 2)) % yeol
                        
                        # 탈출 조건 체크
                        if light[tempi][tempj][tempk] != -1:
                            break
                        else:
                            light[tempi][tempj][tempk] = check
                    check += 1
    
    # 결과 분석을 위한 분리
    temp = []
    for i in range(hang):
        for j in range(yeol):
            for k in range(4):
                temp.append(light[i][j][k])
    
    # 분석 후 정렬 및 반환
    temp = list(Counter(temp).values())
    temp.sort()
    
    return temp
