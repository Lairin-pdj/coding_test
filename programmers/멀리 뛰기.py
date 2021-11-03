def solution(n):
    # dp, i번째 값이 i칸 계단 오르는 방법 수
    count = [1, 1] + [0 for _ in range(n - 1)]
    
    for i in range(2, n + 1):
        # i - 2에서 2칸 뛰는 경우와 i - 1에서 1칸 뛰는 경우 합산
        # 피보나치와 같은 형상
        count[i] = count[i - 1] + count[i - 2]
        # 주어진 조건에 맞도록 나눗셈
        if count[i] > 1234567:
            count[i] = count[i] % 1234567
    
    return count[-1]
