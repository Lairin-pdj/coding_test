def solution(stones, k):
    
    # 정렬된 정도 체크(O(n))
    check = 0
    for a, b in zip(stones[:-1], stones[1:]):
        if a > b:
            check += 1
    
    # 내림차순 정렬에 가까운 경우 뒤집어서 오름차순 정렬에 가깝도록 변경
    if check > len(stones) // 2:
        stones = stones[::-1]
    
    low = 200000000
    low = min(low, max(stones[:k]))
    temp = low
    for i in range(1, len(stones) - k + 1):
        if stones[i + k - 1] > temp:
            # 새로 들어온 돌이 큰 경우 최대값 갱신
            temp = stones[i + k - 1]
        # 빠져나간 돌이 최대값인 경우
        if stones[i - 1] == temp:
            # 최대값 재 탐색(O(n))
            # 내림차순으로 정렬된 경우 최악의 상황 발생
            temp = max(stones[i:i + k])
        
        # 최종 결과 최소값에 반영
        low = min(low, temp)
    
    return low
