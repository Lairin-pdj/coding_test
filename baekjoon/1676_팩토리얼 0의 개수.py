import sys
input = sys.stdin.readline

# 파싱
n = int(input())

# 1 * 2 * 3 * ... * n - 1 * n
# 소인수 분해로 2 * 5 = 10 이 되는 갯수 체크
# 2는 무조건 5보다 많기 때문에 5의 갯수만 체크
answer = 0
while n > 0:
    answer += n // 5
    n = n // 5

# 결과 출력
print(answer)
