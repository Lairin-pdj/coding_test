def solution(s):
    # 공백단위로 분리
    words = s.split(" ")

    # 단어별로 맨 앞 대문자, 그 뒤 소문자
    answer = ''
    for word in words:
        answer += word[:1].upper() + word[1:].lower() + " "

    # 맨 마지막 공백 제거
    answer = answer[:-1]

    # 반환
    return answer
