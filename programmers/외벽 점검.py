from itertools import permutations

def solution(n, weak, dist):
    dist.sort(reverse = True)
    limit = len(weak)
    
    # 친구의 수를 점차적으로 늘려감
    for nums in range(1, len(dist) + 1):
        # 모든 경우의 수를 확인하기위해 순열 적용
        for selected in permutations(dist, nums):
            # 시작점을 바꾸기 위해 limit만큼 반복
            for _ in range(limit):
                i, j = 0, 0
                temp = 0
                # 번갈아가며 크기 비교를 통해 범위 체크 가능 여부 판단
                while i < limit and j < nums:
                    # weak[i]에서 시작해서 j번째 사람의 이동거리로 처리 가능한 범위
                    temp = weak[i] + selected[j]
                    j += 1
                    
                    # 범위 안에 취약지점이 있을 경우 처리
                    while i < limit and weak[i] <= temp:
                        i += 1
            
                    # 전부 처리될 경우 최솟값이기에 바로 반환
                    if i >= limit:
                        return nums
            
                # 시작지점을 뒤로 보내며 원순열 회전
                weak = weak[1:] + [weak[0] + n]
    
    # 불가능할 경우 -1 반환
    return -1
