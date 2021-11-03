def solution(a):
    count = 0
    
    i, j = 0, len(a) - 1
    left, right = a[0], a[-1]           # 왼편과 오른편에 각 각 자기보다 작은 수가 있으면 
    
    while i < j:                        # 모든 경우의 수 체크
        if left > right:
            if left < a[i + 1]:
                count += 1
            else:
                left = a[i + 1]
            i += 1
        else:
            if right < a[j - 1]:
                count += 1
            else:
                right = a[j - 1]
            j -= 1 

    return len(a) - count
