from datetime import datetime, timedelta
import sys
input = sys.stdin.readline

# 파싱
t = int(input())
for _ in range(t):
    b, c = map(int, input().split())
    
    # 입실, 퇴실 시간
    left = []
    right = []
    
    clean = timedelta(hours = c // 60, minutes = c % 60)
    for _ in range(b):
        line = input().rstrip().split()
        
        # 시간처리
        temp = list(map(int, line[1].split("-")))
        temp2 = list(map(int, line[2].split(":")))
        start = datetime(temp[0], temp[1], temp[2], temp2[0], temp2[1])
        temp = list(map(int, line[3].split("-")))
        temp2 = list(map(int, line[4].split(":")))
        end = datetime(temp[0], temp[1], temp[2], temp2[0], temp2[1])
        
        # 입실, 퇴실 처리
        left.append(str(start))
        right.append(str(end + clean))
    
    # 정렬
    left.sort()
    right.sort()
    
    # 최대값 체크
    high, now = 0, 0
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            i += 1
            now += 1
            high = max(high, now)
        elif left[i] > right[j]:
            j += 1
            now -= 1
        else:
            i += 1
            j += 1
    
    # 결과 출력
    print(high)
