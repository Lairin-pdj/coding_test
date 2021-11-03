import re

def solution(new_id):

    # 대문자를 소문자로 치환
    s1 = new_id.lower()
    
    # 특수문자 제거
    s2 = re.sub("[~!@#$%^&*()=+\[{\]}:?,<>/]","", s1)
    
    # 연속된 마침표 한 개로 치환
    s3 = re.sub("[.]+",".", s2)
    
    # 앞과 뒤의 마침표 제거
    s4 = s3
    if s4 != "" and s4[0] == ".":
        s4 = s4[1:]
    if s4 != "" and s4[-1] == ".":
        s4 = s4[:-1]
    
    # 빈 문자열일시 a 대입
    s5 = s4
    if s5 == "":
        s5 += "a"
    
    # 최대 글자수 제한
    s6 = s5
    if len(s6) >= 16:
        s6 = s6[:15]
        if s6[-1] == ".":
            s6 = s6[:-1]
    
    # 최소 글자수 제한 
    s7 = s6
    if len(s7) <= 2:
        while(len(s7) != 3):
            s7 += s7[-1]
    
    # 결과물 반환
    return s7
