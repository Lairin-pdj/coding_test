import math

def solution(n, words):
    dic = {}
    dic[words[0]] = 1

    for i, (a, b) in enumerate(zip(words[:-1], words[1:])):
        # 이어지지 않는 단어를 말한 경우
        if a[-1] != b[0]:
            return [((i + 1) % n) + 1, math.ceil((i + 2) / n)]
        
        # 같은 단어를 말한 경우
        if b in dic:
            return [((i + 1) % n) + 1, math.ceil((i + 2) / n)]
        
        # 정상적인 진행인 경우
        dic[b] = 1

    return [0, 0]
