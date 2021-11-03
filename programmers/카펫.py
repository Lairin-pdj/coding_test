def solution(brown, yellow):
    yak = []
    
    for i in range(1, int(yellow ** 0.5) + 1):      # 노랑의 약수를 구함
        if yellow % i == 0:
            yak.append([i, int(yellow / i)])

    for a, b in yak:                                # 주어진 약수를 토대로 갈색을 추측
        n = b + 2
        m = a + 2
        if n * 2 + m * 2 - 4 == brown:              # 일치할 시 반환
            return [n, m]                           
            
    return 0                                        # 에러시 0 반환
