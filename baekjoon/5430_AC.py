from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

# 테스트 케이스 반복
for _ in range(t):
    # 파싱
    ope = input().rstrip()
    n = int(input())
    # 속도를 위해 deque 사용
    nums = deque()
    if n != 0:
        nums = deque(list(map(int, input().rstrip()[1:-1].split(","))))
    else:
        temp = input()
    
    
    # R 체크용
    isrev = False
    # error 체크용
    dcount = 0
    # 연산 진행
    for i in ope:
        if i == "R":
            # R일 경우 리버스 변경
            if isrev:
                isrev = False
            else:
                isrev = True
        else:
            # 리버스에 따라 앞이나 뒤 숫자 제거
            dcount += 1
            if nums:
                if isrev:
                    nums.pop()
                else:
                    nums.popleft()
    
    # 결과물 출력 
    if dcount > n:
        print("error")
    else:
        if nums:
            if isrev:
                temp = list(nums)[::-1]
                print("[", end = "")
                for i in range(len(temp) - 1):
                    print(temp[i], end = ",")
                print(temp[-1], end = "]\n")
            else:
                temp = list(nums)
                print("[", end = "")
                for i in range(len(temp) - 1):
                    print(temp[i], end = ",")
                print(temp[-1], end = "]\n")
        else:
            print("[]")
