from itertools import combinations

def solution(nums):
    answer = 0

    # 에라스토체네스의 체를 이용한 소수 체크
    maxnum = 3000
    checkarr = [0, 0] + [1] * (maxnum - 1)
    for (i, num) in enumerate(checkarr):
        if num == 1:
            j = i * 2
            while j < maxnum:
                checkarr[j] = 0
                j += i

    # 조합을 이용하여 3개의 합의 소수 판별
    for i, j, k in combinations(nums, 3):
                answer += checkarr[i + j + k]

    return answer
