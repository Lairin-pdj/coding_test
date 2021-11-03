from itertools import combinations

def solution(places):
    answer = []
    
    for room in places:                                     # 장소마다 반복
        participant = []                                    # 사람 좌표 체크
        for x, line in enumerate(room):
            for y, i in enumerate(line):
                if i == "P":
                    participant.append([x, y])
        
        check = True                                        # 거리 2 이하 가림막 체크
        for i in combinations(participant, 2):              # 두 사람의 좌표 조합을 통해 여부 판단
            if abs(i[0][0] - i[1][0]) + abs(i[0][1] - i[1][1]) <= 2:
                if i[0][0] == i[1][0]:
                    if room[i[0][0]][(i[0][1] + i[1][1]) // 2] != "X":
                        check = False
                        break
                elif i[0][1] == i[1][1]:
                    if room[(i[0][0] + i[1][0]) // 2][i[0][1]] != "X":
                        check = False
                        break
                else:
                    if room[i[0][0]][i[1][1]] != "X" or room[i[1][0]][i[0][1]] != "X":
                        check = False
                        break
        
        if check:                                           # 준수 여부 저장
            answer.append(1)
        else:
            answer.append(0)
        
    return answer
