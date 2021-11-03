def solution(n, k, cmd):
    linked = [[i - 1, i + 1, 0] for i in range(n)]                  # [앞, 뒤, 활성화 여부] 형식의 연결리스트 사용
    cursor = k                                                      # 현재 좌표 저장
    stack = []                                                      # 삭제된 행을 보존 하기 위해
    
    for i in cmd:
        ope = i.split(" ")                                          # 주어진 명령어 해석
        if ope[0] == "C":
            if linked[cursor][0] > -1:                              # 연결리스트 수정
                linked[linked[cursor][0]][1] = linked[cursor][1]
            if linked[cursor][1] < n:
                linked[linked[cursor][1]][0] = linked[cursor][0]
            linked[cursor][2] = 1                                   # 비활성화
            stack.append(cursor)                                    # 삭제 스택 추가
            if linked[cursor][1] < n:                               # 커서 위치 변경
                cursor = linked[cursor][1]
            else:
                cursor = linked[cursor][0]
        elif ope[0] == "Z":
            cur = stack.pop()                                       # 스택에서 꺼내와 복원 후 활성화 시킴
            linked[cur][2] = 0
            if linked[cur][0] > -1:
                linked[linked[cur][0]][1] = cur
            if linked[cur][1] < n:
                linked[linked[cur][1]][0] = cur
        elif ope[0] == "U":                                         # 활성화 된 칸만 체크하며 넘어감 
            count = 0
            while count < int(ope[1]):
                count += 1
                cursor = linked[cursor][0]
        elif ope[0] == "D":                                         # 활성화 된 칸만 체크하며 넘어감 
            count = 0
            while count < int(ope[1]):
                count += 1
                cursor = linked[cursor][1]
    temp = ""
    for i in linked:                                                # 활성화 여부를 체크하며 출력문 작성
        if i[2] == 1:
            temp += "X"
        else:
            temp += "O"
    
    return temp
