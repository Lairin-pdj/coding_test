import sys
input = sys.stdin.readline

# 종이 가르기
def div(x, y, r):
    global mone, zero, one

    # 종이 색 확인
    check = True
    temp = nums[x][y]
    for i in range(r):
        for j in range(r):
            if nums[x + i][y + j] != temp:
                check = False
                break

    # 종이가 전부 같은 경우
    if check:
        if temp == 1:
            one += 1
        elif temp == 0:
            zero += 1
        else:
            mone += 1
    # 종이가 다른 경우
    else:
        # 재귀
        for i in range(3):
            for j in range(3):
                div(x + ((r // 3) * i), y + ((r // 3) * j), r // 3)

# 파싱
n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

# 함수 적용
global mone, zero, one
mone, zero, one = 0, 0, 0
div(0, 0, n)

# 결과 출력
print(mone)
print(zero)
print(one)
