import re

def solution(skill, skill_trees):
    
    # 정규식 작성
    line = "[^"
    for i in skill:
        line += i
        line += "|"
    line = line[:-1] + "]"
    
    # 각 스킬트리 체크
    answer = 0
    for tree in skill_trees:
        # 스킬트리와 상관없는 스킬 제거
        temp = re.sub(line, "", tree)
        
        # 차례대로 배우는 것만 체크
        if skill[:len(temp)] == temp:
            answer += 1
    
    return answer
