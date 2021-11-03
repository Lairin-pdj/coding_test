def solution(s):
    length = len(s)
    
    # 길이가 짝수일 때와 아닌 경우를 구분하여 출력
    if length % 2 == 0:
        return s[(length // 2) - 1:(length // 2) + 1]
    else:
        return s[(length // 2)]
