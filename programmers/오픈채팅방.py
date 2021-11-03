def solution(record):
    dic = {}
    
    for i in record:                        # record 분석하여 사전 구성
        c = i.split(' ')
        if c[0] in ["Enter", "Change"]:
            dic[c[1]] = c[2]

            
    answer = []
    
    for i in record:                        # 사전을 토대로 record를 재출력
        c = i.split(' ')
        if c[0] == "Enter":
            answer.append(dic.get(c[1]) + "님이 들어왔습니다.")
        elif c[0] == "Leave":
            answer.append(dic.get(c[1]) + "님이 나갔습니다.")
    
    return answer
