import sys
input = sys.stdin.readline

def nqueen(n, line):
    global count
    now = len(line)
    
    # 성공적으로 퀸을 놓은 경우
    if now == n:
        count += 1
        return
    # 추가로 퀸을 놔야하는 경우
    else:
        # 다음 퀸을 i번째 칸에 놓을 경우
        for i in range(n):
            # 문제가 없는 지 기존의 퀸들과 체크
            flag = True
            for k, j in enumerate(line):
                if i == j or (now - k) == abs(j - i):
                    flag = False
                    break
            
            # 문제가 없을 경우 다음 말을 놓도록 진행
            if flag:
                nqueen(n, line + [i])


n = int(input())
# 갯수 체크용 변수
global count 
count = 0

# 함수 호출
nqueen(n, [])

# 결과 출력
print(count)
