def solution(arr):
    check = arr[:1]
    
    for i in arr[1:]:
        if check[-1] != i:
            check.append(i)
            
    return check
