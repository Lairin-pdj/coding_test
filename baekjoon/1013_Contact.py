import sys
input = sys.stdin.readline

# 파싱
n = int(input())

for _ in range(n):
    signal = input().rstrip()
    
    # 정규식 체크
    length = len(signal)
    idx = 0
    flag = True
    while idx < length:
        # 100+1+
        if idx + 3 <= length and signal[idx:idx + 3] == "100":
            # 첫 1 찾기
            temp = idx + 3
            count = 0
            while temp < length and signal[temp] != "1":
                temp += 1
            # 마지막 1 찾기
            while temp < length and signal[temp] != "0":
                count += 1
                temp += 1
                
            # 뒤에 00이 올 경우
            if temp + 2 <= length and signal[temp:temp + 2] == "00":
                # 여분의 1이 있는 경우
                if count > 1:
                    idx = temp - 1
                # 여분의 1이 없는 경우
                else:
                    flag = False
                    break
            # 뒤에 01이 올 경우
            elif temp + 2 <= length and signal[temp:temp + 2] == "01":
                idx = temp + 2
            # 모자란 경우
            else:
                # 1을 발견 못한 경우
                if count < 1:
                    flag = False
                    break
                else:
                    if temp < length and signal[temp] == "0":
                        flag = False
                        break
                    else:
                        break
        # 01
        elif idx + 2 <= length and signal[idx:idx + 2] == "01":
            idx += 2
        else:
            flag = False
            break
    
    # 결과 출력
    if flag:
        print("YES")
    else:
        print("NO")
