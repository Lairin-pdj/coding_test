def solution(operations):
    queue = []
    
    for ope in operations:
        a, b = ope.split(" ")                           # 명령어 해석
        b = int(b)
        
        if a == "I":
            if len(queue) == 0:                         # 비어있으면 바로 삽입
                queue.append(b)
            else:
                if queue[-1] < b:                       # 맨 뒷값보다 크면 바로 삽입
                    queue.append(b)
                else:
                    for i in range(len(queue)):         # 아닐 경우 순회하며 삽입
                        if queue[i] > b:
                            queue.insert(i, b)
        else:
            if len(queue) != 0:                         # 최대는 맨뒤 최소는 맨앞을 삭제
                if b == 1:
                    queue.pop()
                else:
                    queue.pop(0)
    
    if len(queue) == 0:                                 # 갯수에 맞게 출력
        return [0, 0]
    else:
        return [queue[-1], queue[0]]
