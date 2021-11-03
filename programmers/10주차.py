from itertools import combinations

def solution(line):
    inter = set()
    
    # 교점 체크
    for (a, b, e), (c, d, f) in combinations(line, 2):
        # 평행하지 않을 경우
        if (a * d) - (b * c) != 0:
            x = ((b * f) - (e * d)) / ((a * d) - (b * c))
            y = ((e * c) - (a * f)) / ((a * d) - (b * c))
            
            # 교점이 정수인 경우만 포함
            if float.is_integer(float(x)) and float.is_integer(float(y)):
                inter.add((int(x), int(y)))
    
    # 값 수정을 위한 리스트화
    star = list(inter)
    
    # 최대, 최소 체킹
    xhigh, xlow = -10000000000, 10000000000
    yhigh, ylow = -10000000000, 10000000000
    for x, y in star:
        xhigh = max(xhigh, x)
        xlow = min(xlow, x)
        yhigh = max(yhigh, y)
        ylow = min(ylow, y)
    
    # 좌표 변경
    for i in range(len(star)):
        star[i] = [star[i][0] - xlow, star[i][1] - ylow]
    
    # 문자열 생성
    answer = [["."] * (yhigh - ylow + 1) for _ in range(xhigh - xlow + 1)]
    
    # 교점 대입
    for x, y in star:
        answer[x][y] = "*"
    
    # 방향 전환 및 양식 적용
    answer = list(map(lambda x : "".join(x),list(map(list, zip(*answer)))[::-1]))
    
    # 문자열 반환
    return answer
