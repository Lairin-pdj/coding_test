import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

# n번째 0에 가능한 수 집어넣기
def backtrack(n):
    global sudoku
    global zeros
    global flag
    
    # 이미 완성한 경우 전부 종료
    if flag:
        return
    
    # 완성된 경우
    if n == len(zeros):
        # 출력
        for i in sudoku:
            print(" ".join(map(str, i)))
        
        flag = True
        return
    
    # 가로줄 체크
    temp = set()
    for i in range(9):
        temp.add(sudoku[zeros[n][0]][i])
    set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9} - temp
    
    # 세로줄 체크
    temp = set()
    for i in range(9):
        temp.add(sudoku[i][zeros[n][1]])
    set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9} - temp
    
    # 네모 체크
    x, y = (zeros[n][0] // 3) * 3, (zeros[n][1] // 3) * 3
    temp = set()
    for i in range(3):
        for j in range(3):
            temp.add(sudoku[x + i][y + j])
    set3 = {1, 2, 3, 4, 5, 6, 7, 8, 9} - temp
    
    # 가능한 수 집합 생성
    temp = set1 & set2 & set3
    
    # 다음 0으로 진행
    for i in temp:
        sudoku[zeros[n][0]][zeros[n][1]] = i
        backtrack(n + 1)
        sudoku[zeros[n][0]][zeros[n][1]] = 0

# 주어진 스도쿠 내용 파싱
global sudoku
sudoku = []
for _ in range(9):
    lines = list(map(int, input().split(" ")))
    sudoku.append(lines)

# 0으로 비어있는 부분 좌표 체크
global zeros
zeros = []
for x, line in enumerate(sudoku):
    for y, num in enumerate(line):
        if num == 0:
            zeros.append([x, y])

# 함수 호출
global flag
flag = False
backtrack(0)
