import sys
input = sys.stdin.readline

# 파싱
n = int(input())
m = int(input())
b = set(input().split())

# 100번에서 이동하는 경우
case1 = abs(int(n) - 100)

# 가능 한지 체크 함수
def check(num):
    for i in str(num):
        if i in b:
            return False
    
    return True

# 특정 채널로 변경 후 이동하는 경우
case2 = 1000000
for i in range(1000000):
    # i 아래 체크
    if n - i >= 0 and check(n - i):
        case2 = i + len(str(n - i))
        break
    # i 위 체크
    if check(n + i):
        case2 = i + len(str(n + i))
        break
    
# 결과 출력
print(min(case1, case2))
