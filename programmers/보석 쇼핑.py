from collections import defaultdict

def solution(gems):
    gems_len, gems_kind = len(gems), len(set(gems))

    answer = []
    low = 100000
    
    # 투포인트 탐색
    start, end = 0, 0
    
    # 현재 취한 보석 계산
    bag = defaultdict(int)
    bag[gems[0]] += 1

    while end < gems_len:
        # 가방 안의 보석 종류가 다 있다면
        if len(bag) == gems_kind:
            # 최소값을 계산해서 임시답으로 저장
            if low > end - start:
                low = end - start
                answer = [start + 1, end + 1]
            # 시작 포인트를 움직이며 보석 제거
            bag[gems[start]] -= 1
            # 보석이 없는 경우 숫자로 계산되는 경우을 없애기 위해 사전에서 제거
            if bag[gems[start]] == 0:
                del bag[gems[start]]
            start += 1
        # 없다면
        else:
            # 끝 포인트를 움직이며 보석 추가
            end += 1
            # 맨 마지막 접근 오류를 막기 위해
            if end < gems_len:
                bag[gems[end]] += 1
    
    return answer
