import sys
input = sys.stdin.readline

# 종이 가르기
def div(x, y, r):
    # 종이 색 확인
    check = True
    temp = nums[x][y]
    for i in range(r):
        for j in range(r):
            if nums[x + i][y + j] != temp:
                check = False
    
    # 종이가 전부 같은 경우
    if check:
        if temp == "1":
            print("1", end = "")
        else:
            print("0", end = "")
    # 종이가 다른 경우
    else:
        # 재귀
        print("(", end = "")
        for i in range(2):
            for j in range(2):
                div(x + ((r // 2) * i), y + ((r // 2) * j), r // 2)
        print(")", end = "")

# 파싱
n = int(input())
nums = [input().rstrip() for _ in range(n)]

# 함수 적용
div(0, 0, n)
