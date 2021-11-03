def dfs(depth, amount):                             # 재귀를 이용하여 dfs 탐색
    global answer
    
    if depth == len(number):                        # 전부 체크 후 타겟과 비교
        if amount == k:
            answer += 1
        return
        
    dfs(depth + 1, amount + number[depth])          # 덧셈 및 뺄셈 재귀
    dfs(depth + 1, amount - number[depth])

def solution(numbers, target):                      
    global number                                   # 전역변수들을 활용하여 체크
    number = numbers
    global k
    k = target
    global answer
    answer = 0
    
    dfs(0, 0)

    return answer
