def check(num):
    # 자기자신을 포함하여 1로 시작
    count = 1
    # 1부터 (num // 2) + 1까지 약수의 갯수 체크
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            count += 1
    
    # 약수의 갯수의 짝수, 홀수 구별
    if (count % 2) == 0:
        return True
    else:
        return False

    
def solution(left, right):
    answer = 0
    
    # 주어진 범위의 수 체크
    for i in range(left, right + 1):
        if check(i):
            answer += i
        else:
            answer -= i
    
    return answer
