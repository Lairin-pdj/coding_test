def solution(msg):
    # 인덱스 형성
    index = ["-"]
    for i in range(65, 91):
        index.append(chr(i))
    
    # 글자마다 시작점일 경우 체크
    answer = []
    i = 0    
    while i < len(msg):
        # 인덱스에 없는 글자 찾기
        temp = 0
        while i + 2 + temp <= len(msg) and msg[i:i + 2 + temp] in index:
            temp += 1
        
        # 인덱스에 추가
        index.append(msg[i:i + 2 + temp])
        
        # 확인된 단어 인덱스 추가
        answer.append(index.index(msg[i:i + 1 + temp]))
        
        i += (temp + 1)
        
    return answer
