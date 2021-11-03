import sys
sys.setrecursionlimit(300000)

def star(x, y, k):
    global page
    
    if k == 1:
        # n에 맞춰 위치 측정
        page[x + 1][y + 1] = " "
    else:
        # 가운데 지우기
        temp = 3 ** (k - 1)
        for i in range(temp, 2 * temp):
            for j in range(temp, 2 * temp):
                page[x + i][y + j] = " "
        
        # 분할 재귀
        for i in range(0, 3 * temp, temp):
            for j in range(0, 3 * temp, temp):
                star(x + i, y + j, k - 1)

# 입력 값 저장
n = int(input())

# 별표 도화지 생성
global page
page = [["*"] * n for _ in range(n)]

# k승 체크
k = 0
temp = n
while temp > 1:
    k += 1
    temp /= 3

# 재귀 활용
star(0, 0, k)

# 출력
for i in page:
    print("".join(i))
