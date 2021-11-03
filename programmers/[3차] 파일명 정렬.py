import re

def solution(files):
    answer = []
    temp = []
    
    # 파싱 및 정렬을 위한 형태로 변경
    for order, file in enumerate(files):
        first = re.search("[0-9]", file).start()
        check = re.search("[^0-9]", file[first:])
        # tail이 없는 경우를 대비하여
        if check == None:
            head = file[:first]
            num = file[first:]
            tail = ""
        else:   
            second = first + re.search("[^0-9]", file[first:]).start()
            head = file[:first]
            num = file[first:second]
            tail = file[second:]
        temp.append([head.lower(), int(num), head, num, tail, order])
    
    # 람다를 통한 정렬
    temp.sort(key = lambda x : (x[0], x[1], x[5]))
    
    # 순서대로 정답 정리
    for a, b, head, num, tail, c in temp:
        answer.append(head + num + tail)
        
    return answer
