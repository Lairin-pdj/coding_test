def solution(array, commands):
    answer = []
    
    for a, b, c in commands:
        temp = array[a - 1:b]
        temp.sort()
        answer.append(temp[c - 1])
        
    return answer
