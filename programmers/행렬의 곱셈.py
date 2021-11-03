def solution(arr1, arr2):
    h1 = len(arr1) 
    y1 = len(arr1[0])
    h2 = len(arr2) 
    y2 = len(arr2[0]) 
    
    answer = []
    
    for i in range(h1):
        temp = []
        for j in range(y2):
            num = 0
            for k in range(y1):
                num += arr1[i][k] * arr2[k][j]
            temp.append(num)     
        answer.append(temp)
        
    return answer
