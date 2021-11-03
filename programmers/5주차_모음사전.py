def solution(word):
    words = ["A", "E", "I", "O", "U"]
    level = []
    level.append(words)
    
    # 모든 단어 생성
    for i in range(4):
        temp = []
        for base in level[i]:
            for add in words:
                temp.append(base + add)
        level.append(temp)
    
    # 정렬
    answer = []
    for i in range(5):
        answer.extend(level[i])
    
    answer.sort()
    
    # 위치 정보 반환
    return answer.index(word) + 1
