from itertools import permutations

def solution(numbers):
    answer = set()
    
    check = [0, 0] + [1] * 10000000                         # 최대 9999999까지 가능
    
    for i in range(len(check)):                             # 에라스토테네스의 체를 이용한 소수 판별
        if check[i] != 0:
            temp = i * 2
            while temp < len(check):
                check[temp] = 0
                temp += i
    
    for i in range(len(numbers)):
        for j in list(permutations(numbers, i + 1)):        # 순열을 이용하여 모든 경우의 수 체크
            temp = ''
            for k in j:
                temp += k
            if check[int(temp)] == 1:
                answer.add(int(temp))
    
    return len(answer)
