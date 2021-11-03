def solution(n, times):
    answer = n * times[-1]
    
    times.sort()                            # 정렬 후 이분 탐색 적용
    
    left = 0
    right = n * times[-1]
    mid = (n * times[-1]) // 2
    
    while True:                             # 시간을 변동하면서 알맞은 시간을 탐색
        if left > right:                    # 이분 탐색이 끝나면 탈출
            break
        count = 0
        for i in times:                     # 현재 시간의 체크 가능한 사람 수 계산
            count += mid // i
        
        if count >= n:                      # 비교 후 체크
            answer = min(answer, mid)
            right = mid - 1
            mid = (left + right) // 2
        elif count < n:
            left = mid + 1
            mid = (left + right) // 2
            
    return answer
