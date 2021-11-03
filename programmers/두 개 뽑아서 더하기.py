from itertools import combinations

def solution(numbers):
    answer = set()
    
    # 조합과 집합을 이용하여 값 체크
    for i, j in combinations(numbers, 2):
            answer.add(i + j)

    # 정렬하여 반환
    return sorted(answer)
