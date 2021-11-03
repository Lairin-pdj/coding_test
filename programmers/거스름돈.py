def solution(n, money):
    count = [1] + [0 for _ in range(n)]
    
    # 각 동전을 추가 했을 경우를 계산
    for i in money:
        # i원짜리 동전을 추가해서 j원이 되는 경우의 가짓수 추가
        for j in range(i, n + 1):
            count[j] += count[j - i]
    
    # n원일 경우 가짓 수 반환
    return count[n]
