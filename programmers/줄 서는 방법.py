import math

def solution(n, k):
    # 1부터 n까지의 숫자 배열
    # 남은 숫자들을 보관
    nums = [i for i in range(1, n + 1)]
    
    answer = []
    # 가능한 가짓수를 기반으로 계산하기 위함
    fac = math.factorial(n)
    # 순서대로 n번 뽑기 
    for _ in range(1, n + 1):
        # k번째의 수를 찾기 위해 맨 첫번째부터 규칙 적용
        fac = fac // n
        index = k // fac
        k = k % fac
        # k가 나누어 떨어지는 경우와 아닌경우 나누어 삽입
        if k == 0:
            answer.append(nums.pop(index - 1))
        else :
            answer.append(nums.pop(index))
        n -= 1
        
    return answer
