def solution(arr):
    # 1의 갯수와 0의 갯수 체크
    one = sum(map(sum, arr))
    zero = int(len(arr) ** 2 - one)
    
    # 한단계씩 합치며 확인
    while len(arr) >= 2:
        # 다음 단계 배열을 만들기위한 저장소
        temp = []
        for i in range(0, len(arr), 2):
            line = []
            for j in range(0, len(arr), 2):
                # 모두 같다면
                if arr[i][j] == arr[i + 1][j] == arr[i][j + 1] == arr[i + 1][j + 1]:
                    if arr[i][j] == 1:
                        line.append(1)
                        # 4개가 1개로 합쳐지므로
                        one -= 3
                    elif arr[i][j] == 0:
                        line.append(0)
                        zero -= 3
                    else:
                        # 4개가 같지 않을 경우 다르다는 표식으로 -1 사용
                        line.append(-1)
                else:
                    line.append(-1)
            temp.append(line)
            
        # 다음 단계로 배열 변경
        arr = temp

    return [zero, one]
