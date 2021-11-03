def solution(N, number):
    # dp를 이용하여 풀이
    dp = [0]
    
    # dp[1] ~ dp[8]까지만 체크
    for i in range(1, 9):
        # 집합으로 중복제거
        temp = set()
        
        # "NN...NN" 삽입
        temp.add(int(str(N) * i))
        
        # dp[i] = dp[1]     (+-*/) dp[i - 1] +
        #         dp[2]     (+-*/) dp[i - 2] +
        #         ...                        +
        #         dp[i - 1] (+-*/) dp[1]     
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i - j]:
                    temp.add(k + l)
                    temp.add(k - l)
                    temp.add(k * l)
                    if l != 0:
                        temp.add(k / l)
                        
        # 다음 연산을 위해 저장
        dp.append(temp)
        
        # 목표값이 포함되는지 체크
        if number in dp[i]:
            return i
        
    # 8 안으로 불가능하면 -1 반환
    return  -1
